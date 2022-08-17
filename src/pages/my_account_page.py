import src.pages.main_page as page
from selenium import webdriver
from selenium.webdriver.common.by import By
import src.pages.base_page as base
import time


class MyAccount_page(base.Base_page):
    def __init__(self, driver: webdriver):
        self._driver = driver

    locator = {'home': '//*[@id="center_column"]/ul/li/a',
               'info-account': (By.CLASS_NAME, 'info-account')
               }
    def home(self):
        btn_home = self.find_element(self.locator['home'])
        btn_home.click()
        return page.Main_page(self._driver)

    def assert_result(self):
        text = self.find_element(*self.locator['info-account'])
        assert 'Welcome to your account' in text.text
        time.sleep(3)
        self._driver.quit()