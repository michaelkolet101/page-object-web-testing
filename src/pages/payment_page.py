import src.pages.base_page as base
import src.pages.payment_confirmation_page as page
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Payment_page(base.Base_page):
    def __init__(self, driver: webdriver):
        self._driver = driver

    locator = {'payment_module': (By.CLASS_NAME, 'payment_module'),
               'bankwire': (By.CLASS_NAME, 'bankwire')
               }

    def pay(self):
        pay = self.find_element(*self.locator['payment_module'])
        bankwire = pay.find_element(*self.locator['bankwire'])
        bankwire.click()
        return page.Payment_confirmation(self._driver)

