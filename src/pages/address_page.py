from selenium import webdriver
from selenium.webdriver.common.by import By
import src.pages.shipping_page as page
import src.pages.base_page as base


class Address_page(base.Base_page):

    def __init__(self, driver: webdriver):
        self._driver = driver

    locator = {'checkout_btn': (By.NAME, 'processAddress')}

    def continue_checkout(self):
        standard_checkout = self.find_element(*self.locator['checkout_btn'])
        standard_checkout.click()
        return page.Shipping_page(self._driver)
