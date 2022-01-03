import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Browser:

    def __init__(self, path_driver: str):
        self.path_driver = path_driver
        self.driver = webdriver.Firefox(executable_path=self.path_driver)
        self.driver.implicitly_wait(3)

    def Change_Url(self, Url):
        if self.driver.current_url != Url:
            try:
                self.driver.get(Url)
                return True
            except Exception:
                return False

    def sava_cookie(self, username):
        pickle.dump(self.driver.get_cookies(), open(f"{username}.pkl", "wb"))

    def load__cook(self, username):
        cookies = pickle.load(open(f"{username}.pkl", "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def load_cookies(self, username):
        cookie = pickle.load(open(f"{username}.pkl", "rb"))
        for cook in cookie:
            self.driver.add_cookie(cook)
        self.driver.refresh()

    def Close(self):
        self.driver.close()
        self.driver.quit()


def _write(text: str, element):
    for c in text:
        element.send_keys(c)
        time.sleep(0.07)
