from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class AeriesLogin(object):
    def __init__(self, username, password):
        self.url = "https://aeries.lgsuhsd.org/" + \
        "aeries.net/Loginparent.aspx"
        self.elem = (
            "portalAccountUsername",
            "portalAccountPassword",
            "ctl00_MainContent_lblWelcome"
        )
        self.driver = webdriver.Firefox()
        self.username = username
        self.password = password
        self._write_data()

    def _authenticate(self):
        self.driver.get(self.url)

        user_field = self.driver.find_element_by_id(self.elem[0])
        user_field.send_keys(self.username)
        user_field.send_keys(Keys.RETURN)

        time.sleep(2)
        pass_field = self.driver.find_element_by_id(self.elem[1])
        pass_field.send_keys(self.password)
        pass_field.send_keys(Keys.RETURN)

        self.driver.get("https://aeries.lgsuhsd.org/aeries.net" + \
        "/GradebookSummary.aspx")
        time.sleep(2)

        return self.driver

    def _write_data(self):
        driver = self._authenticate()
        time.sleep(5)
        with open("source.txt", "w+") as f:
            f.write(driver.page_source)
