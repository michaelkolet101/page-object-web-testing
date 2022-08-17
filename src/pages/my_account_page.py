import src.pages.main_page as page
from selenium import webdriver
from selenium.webdriver.common.by import By
import src.pages.base_page as base

class MyAccount_page(base.Base_page):
    def __init__(self, driver: webdriver):
        self._driver = driver

    locator = {'home': (By.XPATH, '//*[@id="center_column"]/ul/li/a')}
    def home(self):
        btn_home = self.find_element(*self.locator['home'])
        btn_home.click()
        return page.Main_page(self._driver)
