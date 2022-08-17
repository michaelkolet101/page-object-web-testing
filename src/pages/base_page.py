
from playwright.sync_api import sync_playwright

class Base_page:
    def __init__(self, driver: sync_playwright):
        self._driver = driver

    def find_element(self, token):
        elem = self._driver.locator(token)
        return elem


