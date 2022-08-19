from playwright.sync_api import sync_playwright
import src.pages.base_page as base
import src.pages.buy_dress_page as page
import time


class Cheap_dress_page(base.Base_page):

    def __init__(self, driver: sync_playwright):
        self._driver = driver
        super().__init__(driver)

    locator = {'checkout': 'text=Proceed to checkout'}

    def buy_the_dress(self):
        submit = self.find_element(self.locator['checkout'])
        submit.click()
        time.sleep(3)

        return page.Buy_dress_page(self._driver)