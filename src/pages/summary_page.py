from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Summary_page:

    def __init__(self, driver: webdriver):
        self._driver = driver

    def continue_checkout(self):
        standard_checkout_1 = self._driver.find_element(By.CLASS_NAME, 'standard-checkout')

        standard_checkout_1.click()
        time.sleep(3)
