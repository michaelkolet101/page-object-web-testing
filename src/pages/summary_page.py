import time

from playwright.sync_api import sync_playwright
import src.pages.base_page as base
import src.pages.address_page as page


class Summary_page(base.Base_page):

    def __init__(self, driver: sync_playwright):
        self._driver = driver
        super().__init__(driver)

    locator = {'checkout_btn': '//*[@id="center_column"]/form/p/button'}
    def continue_checkout(self):
        self._driver.locator(self.locator['checkout_btn']).click()
        time.sleep(3)

        return page.Address_page(self._driver)