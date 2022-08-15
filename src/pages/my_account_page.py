import src.pages.main_page as page
from selenium import webdriver
from selenium.webdriver.common.by import By


class MyAccount_page:
    def __init__(self, driver: webdriver):
        self._driver = driver

    def home(self):
        btn_home = self._driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li/a')
        btn_home.click()
        return page.Main_page(self._driver)
