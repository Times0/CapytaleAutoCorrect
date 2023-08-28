import sys
import time

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QVBoxLayout, QWidget
from qfluentwidgets import InfoBar, InfoBarPosition

from scripts.browser import StudentFileDownloader, User
from views.Ui_window1 import Ui_MainWindow as Window1Ui
from views.Ui_window2 import Ui_MainWindow as Window2Ui

user = User(username="magali.andry-chevalerias", password="Ecedouced#42t")

downloader = StudentFileDownloader()


class AuthWorker(QThread):
    def run(self):
        downloader.auth(user.username, user.password)


class DownloadWorker(QThread):
    progress_signal = pyqtSignal(int)

    def __init__(self, link):
        super().__init__()
        self.link = link

    def run(self):
        # downloader.dl_every_student_file(self.link, max_students=100, progress_signal=self.progress_signal)
        for i in range(100):
            self.progress_signal.emit(i)
            time.sleep(0.3)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setui()
        self.window1_ui.ToolButton_2.clicked.connect(self.check_for_auth_then_download)
        self.start_auth_worker()

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

        self.resize(800, 600)

    def start_auth_worker(self):
        self.auth_worker = AuthWorker()
        self.auth_worker.start(priority=QThread.LowPriority)
        self.auth_worker.finished.connect(self.show_dialog)

    def start_download_worker(self):
        self.download_worker = DownloadWorker(self.window1_ui.LineEdit.text())
        self.download_worker.start(priority=QThread.NormalPriority)
        self.download_worker.progress_signal.connect(self.window2_ui.clicked)

    def check_for_auth_then_download(self):
        if self.auth_worker.isFinished():
            self.start_download_worker()
            self.show_screen(self.window2)
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
