import glob
import importlib.util
import inspect
import logging
import os
import random
from typing import Callable

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%H:%M:%S', filename='logs.log', filemode='w')
logger = logging.getLogger(__name__)


class EvilCorrecter:
    def __init__(self,
                 files_paths: list[str],
                 modele_functions: dict[str, Callable] = None,
                 ):
        self.student_names: list[str] = [extract_name(path) for path in files_paths]
        self.file_path: dict[str, str] = dict(zip(self.student_names, files_paths))
        logger.debug(f"Students names: {self.student_names}")

        self.modele_functions: dict[str, Callable] = modele_functions  # {function_name: modele_function}
        self.funtions_names_to_test: list[str] = list(modele_functions.keys())

        self.test_values: dict[str, dict[str:tuple]] = {}  # {function_name: {test_name: test_values}}
        self.expected_outputs: dict[str, dict[str, any]] = {}  # {function_name: {test_name: expected_output}}

        self.check_parameters()
        self.generate_tests(nb_tests_per_f=5)
        self.generate_expected_outputs()

        # Output of the tests
        self.detailed_results: dict[
            str, dict[str, dict[str, Result]]] = {}  # {student_name: {function_name: {test_name: result}}}

    def check_parameters(self):
        assert self.modele_functions is not None, "Please provide modele_functions"
        assert self.funtions_names_to_test is not None, "Please provide funtions_names_to_test"

    def generate_tests(self, nb_tests_per_f: int):
        """Generate tests from a function with type annotations
        :return: tuple containing all the args for one test
        """
        for f in self.modele_functions.values():
            logger.debug(f"Generating {nb_tests_per_f} tests for function {f.__name__}")
            tests = {}
            logger.debug(f"Function annotations: {f.__annotations__}")

            for i in range(nb_tests_per_f):
                test = []
                for param_name, param_type in f.__annotations__.items():
                    if param_type in TEST_GENERATOR:
                        test.append(TEST_GENERATOR[param_type]())
                    else:
                        raise TypeError(f"Type {param_type} not supported")

                tests[f"test_{i}"] = tuple(test)

            logger.debug(f"Generated tests: {tests}")
            self.test_values[f.__name__] = tests

    def generate_expected_outputs(self):
        for function_name in self.funtions_names_to_test:
            self.expected_outputs[function_name] = {}
            for test_name in self.test_values[function_name]:
                self.expected_outputs[function_name][test_name] = self.modele_functions[function_name] \
                    (*self.test_values[function_name][test_name])

    def test_student(self, student_name: str) -> None:
        logger.debug(f"Testing student {student_name}")
        file = self.file_path[student_name]
        self.detailed_results[student_name] = {}
        for function_name in self.funtions_names_to_test:
            self.detailed_results[student_name][function_name] = {}
            try:
                function = load_function(file, function_name)
            except AttributeError:
                logger.debug(f"Function {function_name} not found in {file}, skipping")
                for test_name in self.expected_outputs[function_name]:
                    self.detailed_results[student_name][function_name][test_name] = Result.INEXSISTANT
                continue
            # Generate tests from modele function because it has type annotations
            self.test_function(function, self.test_values[function_name], student_name)

    def test_function(self, function: Callable, tests: dict[str, tuple], student_name) -> None:
        logger.debug(f"Testing function {function.__name__}")
        for test_name, test in tests.items():
            logger.debug(f"Testing {test_name} with {test}")
            try:
                result = run_with_timeout(function, *test)

            except TimeoutError:
                self.detailed_results[student_name][function.__name__][test_name] = Result.TIMEOUT
                continue

            except Exception as e:
                logger.debug(f"Error {e} while testing {function.__name__} with {test}, result -> ERROR")
                self.detailed_results[student_name][function.__name__][test_name] = Result.ERROR
                continue

            if result == self.expected_outputs[function.__name__][test_name]:
                self.detailed_results[student_name][function.__name__][test_name] = Result.OK
            else:
                self.detailed_results[student_name][function.__name__][test_name] = Result.WRONG


import multiprocess


def timeout(func, timeout_sec=1, *args, **kwargs):
    with multiprocess.Pool(processes=1) as pool:
        result = pool.apply_async(func, args=args, kwds=kwargs)
        try:
            return result.get(timeout_sec)
        except multiprocess.TimeoutError:
            raise TimeoutError


def run_with_timeout(func, *args, **kwargs):
    return timeout(func, 0.5, *args, **kwargs)


def random_int():
    return random.randint(0, 100)


def random_float():
    return random.uniform(0, 100)


def random_str():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))


def random_list():
    return [random.randint(0, 100) for _ in range(random.randint(1, 10))]


def wrap_test(prev: any) -> tuple:
    return (prev,)


def nb_params(func):
    return len(inspect.signature(func).parameters)


TEST_GENERATOR = {
    int: random_int,
    float: random_float,
    str: random_str,
    list: random_list,
}


def extract_name(path: str) -> str:
    return path.split('\\')[-1].split('.')[0]


from enum import Enum, auto


class Result(Enum):
    OK = auto()
    WRONG = auto()
    ERROR = auto()
    TIMEOUT = auto()
    INEXSISTANT = auto()


def load_function(file: str, function_name: str) -> Callable:
    spec = importlib.util.spec_from_file_location(function_name, file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, function_name)


def get_functions_from_file(file: str) -> dict[str, Callable]:
    spec = importlib.util.spec_from_file_location("module.name", file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return {name: function for name, function in module.__dict__.items() if callable(function)}


if __name__ == '__main__':
    cwd = os.path.dirname(os.path.realpath(__file__))
    files = glob.glob(os.path.join(cwd, "..", "tests", "copies", "*.py"))
    correcter = EvilCorrecter(files_paths=files,
                              modele_functions=get_functions_from_file(
                                  os.path.join(cwd, "..", "tests", "correction.py")))
    correcter.test_student('Jean Jacques')
    correcter.test_student('Mich Mich')

    from pprint import pprint

    pprint(correcter.detailed_results)
