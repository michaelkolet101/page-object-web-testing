
from playwright.sync_api import sync_playwright

class Base_page:

    def __init__(self, driver: sync_playwright):
        self._driver = driver

    def find_element(self, token: str):
        elem = self._driver.locator(token)
        return elem

    def wait_element(self, token: str):
        elem = self._driver.wait_for_selector(token)
        return elem


