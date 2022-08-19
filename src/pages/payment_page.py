import src.pages.base_page as base
import src.pages.payment_confirmation_page as page
from playwright.sync_api import sync_playwright

import time


class Payment_page(base.Base_page):
    def __init__(self, driver: sync_playwright):
        self._driver = driver
        super().__init__(driver)

    locator = {'payment_module': '.payment_module',
               'bankwire': '.bankwire'
               }

    def pay(self):
        pay = self.wait_element(self.locator['payment_module'])
        bankwire = pay.wait_for_selector(self.locator['bankwire'])
        bankwire.click()
        return page.Payment_confirmation(self._driver)

