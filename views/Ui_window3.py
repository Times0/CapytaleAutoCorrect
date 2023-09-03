import importlib
import logging
import os
from importlib.machinery import SourceFileLoader
from typing import Callable

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout
from qfluentwidgets import PushButton, TitleLabel, InfoBar, InfoBarPosition, ProgressBar

logger = logging.getLogger(__name__)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.parent = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 592)

        centralWidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(centralWidget)

        layout = QVBoxLayout(centralWidget)

        # Add a label to display the instruction
        self.instructionLabel = TitleLabel("Please select the Python file (.py) for test correction:")
        layout.addWidget(self.instructionLabel)

        # Add a button to open file dialog
        self.openFileButton = PushButton("Select File")
        self.openFileButton.clicked.connect(self.open_file_dialog)
        layout.addWidget(self.openFileButton)

        # Removed the label that displays the selected file

        # Add a button to initiate the correction, but hide it initially
        self.correctNowButton = PushButton("Correct now")
        self.correctNowButton.setFixedSize(200, 60)  # Make the button bigger
        self.correctNowButton.hide()
        layout.addWidget(self.correctNowButton)

        # Add a loading bar to display the progress
        self.progressBar = ProgressBar()
        self.progressBar.hide()
        layout.addWidget(self.progressBar)

        self.correction_path = None
        # Fill remaining space

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Test Correction File Selector"))

    def update_progress_bar(self, value: int):
        print(value)
        self.progressBar.setValue(value)

    def open_file_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Select Python File",
            "",
            "Python Files (*.py);;All Files (*)",
            options=options
        )

        if filename:
            logger.info(f"Selected file: {filename}")
            # No longer displaying the selected file name
            self.check_file(filename)

    def check_file(self, filename) -> None:
        # Placeholder function for the actual file checking logic
        logger.info("Checking file...")
        # retrieve the "tests" dict from the modele file
        name = os.path.basename(filename)
        correction = SourceFileLoader(name, filename).load_module()
        try:
            tests = correction.tests
        except AttributeError:
            logger.debug(f"Tests not found in {filename}, please add a 'tests' dict")
            InfoBar.error(
                title='Selected file is not valid',
                content=f"Tests not found in {filename}, please add a 'tests' dict",
                position=InfoBarPosition.BOTTOM,
                parent=self.parent,
                duration=5000
            )
            return

        # Verify that the file contains the required functions
        functions = get_functions_from_file(filename)
        for function_name in tests:
            if function_name not in functions:
                logger.debug(f"Function {function_name} not found in {filename}, please add it")
                InfoBar.error(
                    title='Selected file is not valid',
                    content=f"Function {function_name} not found in {filename}, please add it",
                    position=InfoBarPosition.BOTTOM,
                    parent=self.parent,
                    duration=5000
                )
                return

        InfoBar.success(
            title="The correction file is valid 🔥",
            content="The selected file is valid, you can now start the test correction",
            position=InfoBarPosition.BOTTOM,
            parent=self.parent,
            duration=5000
        )
        self.correction_path = filename
        self.correctNowButton.show()
        self.progressBar.show()


def get_functions_from_file(file: str) -> dict[str, Callable]:
    spec = importlib.util.spec_from_file_location("module.name", file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return {name: function for name, function in module.__dict__.items() if callable(function)}


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.retranslateUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
