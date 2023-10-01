import glob
import logging
import os
import time
import dotenv

import attr
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

from scripts import utils

logger = logging.getLogger(__name__)

# exclude selenium logs
logging.getLogger('selenium').setLevel(logging.WARNING)


@attr.s
class User:
    username: str = attr.ib(default=None)
    password: str = attr.ib(default=None)


dotenv.load_dotenv()
user = User(username=os.getenv("ENT_USERNAME"), password=os.getenv("ENT_PASSWORD"))
print(user)


class StudentFileDownloader:
    def __init__(self, dl_path=None):
        self.driver = None

        self.dl_path = dl_path
        self.copies_path = None
        self.options = self._setup_browser_options()

    def _setup_browser_options(self):
        options = Options()
        options.add_argument('-headless')

        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain")
        options.set_preference("browser.download.dir", self.dl_path)
        return options

    def auth(self, identifiant, password):
        self.driver = webdriver.Firefox(options=self.options)
        self.driver.get("https://ent.iledefrance.fr/auth/login")
        time.sleep(2)
        self.driver.find_element(By.ID, "email").send_keys(identifiant)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
        # Wait for the page to load
        time.sleep(2)
        assert self.driver.current_url == "https://ent.iledefrance.fr/timeline/timeline"
        self.driver.get("https://capytale2.ac-paris.fr/web/c-auth/pvd/mln/connect")
        self.driver.get("https://capytale2.ac-paris.fr/web/my")
        print("Successfully logged in.")

    def dl_every_student_file(self, assignment_link, copies_path, progress_signal=None) -> None:
        self.copies_path = copies_path
        # create folder if it does not exist

        self.driver.get(assignment_link)
        time.sleep(0.5)
        self.dl_csv()
        time.sleep(0.5)
        names: list[str] = utils.extract_names_from_csv(f"{self.dl_path}/CAPYTALE.csv")
        logger.info(f"Found {len(names)} students")
        logger.debug(names)
        logger.info("Downloading files...")
        if not os.path.exists(self.copies_path):
            os.makedirs(self.copies_path)
        for name in names:
            if progress_signal:
                progress_signal.emit(names.index(name))
            if self._is_file_already_downloaded(name):
                logger.debug(f"Skipping {name}")
                continue
            time.sleep(0.5)

            copie_link = self.driver.find_element(By.LINK_TEXT, name)
            try:
                self.driver.execute_script("arguments[0].scrollIntoView();", copie_link)
            except selenium.common.exceptions.ElementNotInteractableException:
                logger.warning(f"Could not scroll to {name}, retrying...")
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
            time.sleep(0.5)
            copie_link.click()
            self.inside_basthon(name)

    def inside_basthon(self, student_name):
        self.wait_for_page_to_be_fully_loaded()
        MAX_ATTEMPTS = 5
        attempt_count = 0
        while attempt_count < MAX_ATTEMPTS:
            time.sleep(1)
            try:
                self.driver.find_element(By.ID, "download").click()
                time.sleep(0.5)
                logging.info(f"Downloaded {student_name}'s file")
                self.rename_last_downloaded_file(student_name)
                break
            except selenium.common.exceptions.ElementClickInterceptedException:
                attempt_count += 1
                logging.warning(f"Could not download {student_name}'s file, retrying...")
                continue

        if attempt_count == MAX_ATTEMPTS:
            logging.error(f"Could not download {student_name}'s file")

        self.driver.find_element(By.XPATH, "//a/button/i").click()  # Retour à la liste des élèves

    def dl_csv(self):
        if os.path.exists(self.dl_path + "/CAPYTALE.csv"):
            os.remove(self.dl_path + "/CAPYTALE.csv")
        self.driver.find_element(By.CSS_SELECTOR, ".dt-button > span").click()

    def _is_file_already_downloaded(self, student_name):
        return os.path.exists(f"{self.copies_path}/{student_name}.py")

    def rename_last_downloaded_file(self, student_name):
        list_of_files = glob.glob(f"{self.dl_path}/*.py")
        latest_file = max(list_of_files, key=os.path.getctime)

        os.rename(latest_file, f"{self.copies_path}/{student_name}.py")
        logger.debug(f"Renamed {latest_file} to {student_name}.py")

    @staticmethod
    def _inverse_name(name):
        for i in range(len(name)):
            if name[i] == " ":
                return name[i + 1:] + " " + name[:i]
        return name

    def __del__(self):
        if self.driver:
            self.driver.quit()

    def wait_for_page_to_be_fully_loaded(self):
        time.sleep(3)


if __name__ == '__main__':
    downloader = StudentFileDownloader()
    downloader.auth(user.username, user.password)
    downloader.dl_every_student_file("https://capytale2.ac-paris.fr/web/assignments/216298")
    input("Press enter to continue...")
