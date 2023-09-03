import glob
import logging
import os
import sys

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QVBoxLayout, QWidget
from qfluentwidgets import InfoBar, InfoBarPosition

from scripts.browser import StudentFileDownloader, User
from scripts.tests_better import EvilCorrecter
from views.Ui_window1 import Ui_MainWindow as Window1Ui
from views.Ui_window2 import Ui_MainWindow as Window2Ui
from views.Ui_window3 import Ui_MainWindow as Window3Ui

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%H:%M:%S',
                    handlers=[logging.StreamHandler(), logging.FileHandler("logs.log")])

logger = logging.getLogger(__name__)
user = User(username="magali.andry-chevalerias", password="Ecedouced#42T")

cwd = os.path.dirname(os.path.realpath(__file__))

downloader = StudentFileDownloader(dl_path=os.path.join(cwd, "scripts", "downloads"))


class AuthWorker(QThread):
    def run(self):
        downloader.auth(user.username, user.password)


class DownloadWorker(QThread):
    progress_signal = pyqtSignal(int)

    def __init__(self, link, copies_path):
        super().__init__()
        self.link = link
        self.copies_path = copies_path

    def run(self):
        downloader.dl_every_student_file(self.link, self.copies_path, self.progress_signal)


class CorrectWorker(QThread):
    progress_signal = pyqtSignal(int)

    def __init__(self, copies_paths, output_path, correction_file):
        super().__init__()
        self.output_path = output_path
        self.correction_file = correction_file
        self.copies_paths = copies_paths

    def run(self) -> None:
        correcter = EvilCorrecter(self.copies_paths, self.correction_file)
        correcter.correct_all(progress_signal=self.progress_signal)
        correcter.generate_xlsx(self.output_path)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setui()
        self.window1_ui.ToolButton_2.clicked.connect(self.check_for_auth_then_download)
        self.window2_ui.PushButton.clicked.connect(lambda: self.show_screen(self.window3))
        self.start_auth_worker()

        self.copies_path = None

    def setui(self):
        self.setWindowTitle("Capytale auto correc")

        # Central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Stacked widget to switch between windows
        self.stacked_widget = QStackedWidget(self)
        self.layout.addWidget(self.stacked_widget)

        # Window 1 setup
        self.window1 = QMainWindow()
        self.window1_ui = Window1Ui()
        self.window1_ui.setupUi(self.window1)  # Pass window1 widget
        self.stacked_widget.addWidget(self.window1)  # Add window1 to the stacked widget

        # Window 2 setup
        self.window2 = QMainWindow()
        self.window2_ui = Window2Ui()
        self.window2_ui.setupUi(self.window2)  # Pass window2 widget
        self.stacked_widget.addWidget(self.window2)  # Add window2 to the stacked widget

        # Window 3 setup
        self.window3 = QMainWindow()
        self.window3_ui = Window3Ui()
        self.window3_ui.setupUi(self.window3)  # Pass window3 widget
        self.stacked_widget.addWidget(self.window3)  # Add window3 to the stacked widget
        self.window3_ui.correctNowButton.clicked.connect(self.start_correct_worker)

        self.stacked_widget.setCurrentWidget(self.window1)

        self.resize(800, 600)

    def start_auth_worker(self):
        self.auth_worker = AuthWorker()
        self.auth_worker.start(priority=QThread.NormalPriority)
        self.auth_worker.finished.connect(self.show_dialog)

    def start_download_worker(self):
        link = self.window1_ui.LineEdit.text()
        self.copies_path = os.path.join(cwd, "copies", link.split("/")[-1])
        self.download_worker = DownloadWorker(link, copies_path=self.copies_path)
        logger.info(f"Copies path: {self.copies_path}")
        self.download_worker.start(priority=QThread.NormalPriority)
        self.download_worker.progress_signal.connect(self.window2_ui.clicked)

    def start_correct_worker(self):
        self.correct_worker = CorrectWorker(
            copies_paths=glob.glob(os.path.join(cwd, self.copies_path, "*.py")),
            output_path="output/corrected.xlsx",
            correction_file=self.window3_ui.correction_path
        )
        self.correct_worker.start(priority=QThread.HighestPriority)
        self.correct_worker.progress_signal.connect(self.window3_ui.update_progress_bar)
        self.correct_worker.finished.connect(self.end)

    def check_for_auth_then_download(self):
        if self.auth_worker.isFinished():
            self.start_download_worker()
            self.show_screen(self.window2)
            self.window2_ui.set_copies_path(self.copies_path)
        else:
            InfoBar.error(
                title='',
                content="The authentication is still in progress. Please wait.",
                isClosable=True,
                position=InfoBarPosition.BOTTOM_RIGHT,
                duration=3000,
                parent=self
            )

    def show_screen(self, screen):
        self.stacked_widget.setCurrentWidget(screen)

    def show_dialog(self):
        InfoBar.success(
            title='',
            content="The authentication was successful.",
            isClosable=True,
            position=InfoBarPosition.BOTTOM_RIGHT,
            duration=3000,
            parent=self
        )

    def end(self):
        InfoBar.success(
            title='',
            content="The correction is finished. You can find the output file in the output folder.",
            isClosable=True,
            position=InfoBarPosition.BOTTOM_RIGHT,
            duration=3000,
            parent=self
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
