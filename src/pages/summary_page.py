from selenium import webdriver
from selenium.webdriver.common.by import By
import src.pages.base_page as base
import src.pages.address_page as page


class Summary_page(base.Base_page):

    def __init__(self, driver: webdriver):
        self._driver = driver

    locator = {'checkout_btn': (By.CLASS_NAME, 'standard-checkout')}

    def continue_checkout(self):
        standard_checkout_1 = self.find_element(*self.locator['checkout_btn'])
        standard_checkout_1.click()

        return page.Address_page(self._driver)