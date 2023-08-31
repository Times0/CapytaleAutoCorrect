import glob
import logging
import os
import time

import attr
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    filename='logs.log', filemode='w')

logger = logging.getLogger(__name__)


@attr.s
class User:
    username: str = attr.ib(default=None)
    password: str = attr.ib(default=None)


user = User(username="magali.andry-chevalerias", password="Ecedouced#42T")


class StudentFileDownloader:
    def __init__(self):
        self.options = self._setup_browser_options()
        self.driver = None

    @staticmethod
    def _setup_browser_options():
        options = Options()
        # If you want headless mode, uncomment the next line
        # options.add_argument('-headless')

        # Set preferences directly on the options object
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain")
        download_path = os.path.join(os.getcwd(), "copies")
        options.set_preference("browser.download.dir", download_path)

        return options

    def auth(self, identifiant, password):
        self.driver = webdriver.Firefox(options=self.options)
        self.driver.get("https://ent.iledefrance.fr/auth/login")
        time.sleep(1)
        self.driver.find_element(By.ID, "email").send_keys(identifiant)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
        # Wait for the page to load
        time.sleep(2)
        assert self.driver.current_url == "https://ent.iledefrance.fr/timeline/timeline"
        self.driver.get("https://capytale2.ac-paris.fr/web/c-auth/pvd/mln/connect")
        self.driver.get("https://capytale2.ac-paris.fr/web/my")
        print("Successfully logged in.")

    def dl_every_student_file(self, assignment_link, max_students=100, progress_signal=None):
        self.driver.get(assignment_link)
        input("Press enter to continue...")
        chosen_file_path = ""

        for i in range(2, max_students):
            time.sleep(0.5)
            if progress_signal:
                progress_signal.emit(int(100 * i / max_students))
            try:
                element = self.driver.find_element(By.LINK_TEXT, "BAH Gérard")
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                time.sleep(1)
                element.click()
            except Exception as e:
                print(e)
                continue

            self._download_and_rename_file(chosen_file_path)

        if progress_signal:
            progress_signal.emit(100)
        print("Successfully downloaded every file.")
        self.driver.quit()

    @staticmethod
    def _is_file_already_downloaded(student_name):
        return rf"copies\{student_name}.py" in glob.glob("copies/*.py")

    def _get_student_name(self):
        student_name_element = self.driver.find_element(By.ID, "capytale-student-info")
        student_name_text = student_name_element.text
        return self._inverse_name(student_name_text[:-7]).replace(" ", "_")

    def _download_and_rename_file(self, chosen_file_path):
        MAX_ATTEMPTS = 5  # define a max number of attempts to avoid infinite loops
        attempts = 0

        while attempts < MAX_ATTEMPTS:
            try:
                time.sleep(0.2)
                student_name = self._get_student_name()
                if len(student_name) < 3:
                    attempts += 1
                    continue

                if self._is_file_already_downloaded(student_name):
                    print(f"Skipping {student_name}")
                    self.driver.find_element(By.XPATH, "//a/button/i").click()
                    time.sleep(1)
                    return
                else:
                    self.driver.find_element(By.ID, "download").click()
                    time.sleep(0.5)
                    print(f"Downloaded {student_name}'s file")

                    if not chosen_file_path:
                        list_of_files = glob.glob('copies/*.py')
                        latest_file = max(list_of_files, key=os.path.getctime)
                        chosen_file_path = latest_file

                    os.rename(chosen_file_path, fr"copies\{student_name}.py")
                    self.driver.find_element(By.XPATH, "//a/button/i").click()
                    time.sleep(1)
                    break

            except NoSuchElementException:  # capture specific exception
                attempts += 1

            except Exception as e:  # it's good to know what unexpected errors occur
                print(f"Unexpected error: {e}")
                attempts += 1

    @staticmethod
    def _inverse_name(name):
        for i in range(len(name)):
            if name[i] == " ":
                return name[i + 1:] + " " + name[:i]
        return name

    def run(self, assignment_link):
        # MODIFY HERE: username, password
        self.auth(user.username, user.password)
        self.dl_every_student_file(assignment_link, max_students=100)

    def __del__(self):
        # Destructor to close the browser instance
        if self.driver:
            self.driver.quit()


if __name__ == '__main__':
    downloader = StudentFileDownloader()
    downloader.auth(user.username, user.password)
    downloader.dl_every_student_file("https://capytale2.ac-paris.fr/web/assignments/1608018")
    input("Press enter to continue...")
