import glob
import importlib.util
import logging
import os
from enum import Enum, auto
from importlib.machinery import SourceFileLoader
from pprint import pprint
from typing import Callable

import multiprocess
import xlsxwriter

logger = logging.getLogger(__name__)


class EvilCorrecter:
    def __init__(self,
                 files_paths: list[str],
                 correction_path: str,
                 ):
        self.student_names: list[str] = [extract_name(path) for path in files_paths]
        self.file_path: dict[str, str] = dict(zip(self.student_names, files_paths))
        logger.debug(f"Students names: {self.student_names}")

        self.correction_file: str = correction_path
        self.model_functions: dict[str, Callable] = get_functions_from_file(self.correction_file)
        self.funtions_names_to_test: list[str] = list(self.model_functions.keys())

        self.test_values: dict[str, dict[str:tuple]] = {}  # {function_name: {test_name: test_values}}
        self.expected_outputs: dict[str, dict[str, any]] = {}  # {function_name: {test_name: expected_output}}

        self.check_parameters()
        self.generate_tests()
        self.generate_expected_outputs()

        # Output of the tests
        self.detailed_results: dict[
            str, dict[str, dict[str, Result]]] = {}  # {student_name: {function_name: {test_name: result}}}

    def check_parameters(self):
        assert self.model_functions is not None, "Please provide model_functions"
        assert self.funtions_names_to_test is not None, "Please provide funtions_names_to_test"

    def generate_tests(self):
        """Generate tests from a function with type annotations
        :return: tuple containing all the args for one test
        """

        # retrieve the "tests" dict from the modele file
        name = os.path.basename(self.correction_file)
        correction = SourceFileLoader(name, self.correction_file).load_module()
        try:
            tests = correction.tests
        except AttributeError:
            logger.debug(f"Tests not found in {self.correction_file}, please add a 'tests' dict")
            return

        for f_name in tests.keys():
            self.test_values[f_name] = {}
            for i, test in enumerate(tests[f_name]):
                self.test_values[f_name][f"test {i}"] = test

    def generate_expected_outputs(self):
        for function_name in self.funtions_names_to_test:
            self.expected_outputs[function_name] = {}
            for test_name in self.test_values[function_name]:
                args = self.test_values[function_name][test_name]
                if isinstance(args, tuple):
                    self.expected_outputs[function_name][test_name] = self.model_functions[function_name](*args)
                else:
                    self.expected_outputs[function_name][test_name] = self.model_functions[function_name](args)

    def correct_student(self, student_name: str) -> None:
        logger.debug(f"Testing student {student_name}")
        file = self.file_path[student_name]
        self.detailed_results[student_name] = {f_name: {} for f_name in self.funtions_names_to_test}
        if self.test_for_inputs(file, student_name):
            return
        for function_name in self.funtions_names_to_test:
            try:
                function = load_function(file, function_name)
            except AttributeError:
                logger.debug(f"Function {function_name} not found in {file}, skipping")
                for test_name in self.expected_outputs[function_name]:
                    self.detailed_results[student_name][function_name][test_name] = Result.INEXSISTANT
                continue
            except SyntaxError:
                logger.debug(f"Syntax error in {file}, skipping")
                for test_name in self.expected_outputs[function_name]:
                    self.detailed_results[student_name][function_name][test_name] = Result.SYNTAX_ERROR
                continue
            # Generate tests from modele function because it has type annotations
            self.correct_function(function, self.test_values[function_name], student_name)

    def correct_function(self, function: Callable, tests: dict[str, tuple], student_name) -> None:
        # logger.debug(f"Testing function {function.__name__}")
        for test_name, test in tests.items():
            logger.debug(f"Testing {test_name} with {test}")
            try:
                if isinstance(test, tuple):
                    result = run_without_timeout(function, *test)
                else:
                    result = run_without_timeout(function, test)
            except TimeoutError:
                self.detailed_results[student_name][function.__name__][test_name] = Result.TIMEOUT
                logger.info(f"Timeout while testing {function.__name__} with {test}, result -> TIMEOUT")
                continue

            except Exception as e:
                logger.debug(f"Error {e} while testing {function.__name__} with {test}, result -> ERROR")
                self.detailed_results[student_name][function.__name__][test_name] = Result.ERROR
                continue

            if result == self.expected_outputs[function.__name__][test_name]:
                self.detailed_results[student_name][function.__name__][test_name] = Result.OK
            else:
                self.detailed_results[student_name][function.__name__][test_name] = Result.WRONG
                logger.info(f"Error while testing {function.__name__} from {student_name} with {test}")
                logger.info(f"Expected {self.expected_outputs[function.__name__][test_name]} but got {result}")

    def correct_all(self, progress_signal=None):
        for student_name in self.student_names:
            self.correct_student(student_name)
            if progress_signal:
                progress = self.student_names.index(student_name) / len(self.student_names) * 100
                progress_signal.emit(int(progress))
                print(f"Finished {student_name}, progress: {progress}%")

    def generate_xlsx(self, path):
        print("Generating xlsx")
        workbook = xlsxwriter.Workbook(path)
        worksheet = workbook.add_worksheet()

        # Create a format for cell coloring
        pass_format = workbook.add_format({'bg_color': '#C6EFCE', 'bold': True})
        fail_format = workbook.add_format({'bg_color': '#FFC7CE', 'bold': True})

        # Start from the first cell. Rows and columns are zero-indexed.
        row = 0
        col = 0

        # Iterate over the data and write it out row by row.
        for student_name, functions in self.detailed_results.items():
            worksheet.write(row, col, student_name)
            row += 1

            for function_name, tests in functions.items():
                worksheet.write(row, col + 1, function_name)
                row += 1

                for test_name, result in tests.items():
                    worksheet.write(row, col + 2, test_name)
                    worksheet.write(row, col + 3, result.name)

                    passed = result == Result.OK

                    # Check if the test passed and apply the corresponding cell color
                    if passed:
                        worksheet.set_row(row, cell_format=pass_format)
                    else:
                        worksheet.set_row(row, cell_format=fail_format)

                    row += 1

            # Add a separator (blank row) between students
            row += 1

        workbook.close()

    def test_for_inputs(self, file, student_name):
        """Test if the files contains the keyword input and raise an error if it does"""
        with open(file, 'r') as f:
            content = f.read()
            if "input" in content:
                logger.debug(f"Found input in {file}, please remove it")
                for function_name in self.funtions_names_to_test:
                    for test_name in self.expected_outputs[function_name]:
                        self.detailed_results[student_name][function_name][test_name] = Result.INPUT_FOUND
                return True
        return False


def timeout(func, timeout_sec, *args, **kwargs):
    with multiprocess.Pool(processes=1) as pool:
        result = pool.apply_async(func, args=args, kwds=kwargs)
        try:
            return result.get(timeout_sec)
        except multiprocess.TimeoutError:
            raise TimeoutError


def run_with_timeout(func, *args, **kwargs):
    return timeout(func, 2, *args, **kwargs)


def run_without_timeout(func, *args, **kwargs):
    return func(*args, **kwargs)


def extract_name(path: str) -> str:
    return path.split('\\')[-1].split('.')[0]


class Result(Enum):
    OK = "OK"
    WRONG = "Wrong output"
    ERROR = "Error"
    TIMEOUT = "Timeout"
    INEXSISTANT = "Inexistant"
    SYNTAX_ERROR = "Syntax error"
    INPUT_FOUND = "'Input' found in file"


def load_function(file: str, function_name: str) -> Callable:
    spec = importlib.util.spec_from_file_location(function_name, file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    f = getattr(module, function_name)
    if not isinstance(f, Callable):
        raise AttributeError
    return f


def get_functions_from_file(file: str) -> dict[str, Callable]:
    spec = importlib.util.spec_from_file_location("module.name", file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return {name: function for name, function in module.__dict__.items() if callable(function)}


if __name__ == '__main__':
    logger.info("Starting tests")
    copies_path = rf"../copies/1911196"
    correction_file = os.path.join(os.getcwd(), "../correction_1.py")

    copies = glob.glob(f"{copies_path}/*.py")

    correcter = EvilCorrecter(files_paths=copies, correction_path=correction_file)

    correcter.correct_all()
