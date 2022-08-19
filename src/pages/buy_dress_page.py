from playwright.sync_api import sync_playwright
import src.pages.summary_page as page
import src.pages.base_page as base
import time


class Buy_dress_page(base.Base_page):

    def __init__(self, driver: sync_playwright):
        self._driver = driver
        super().__init__(driver)

    locator = {'checkout': '// *[ @ id = "center_column"] / p[2] / a[1]'
               }
    def continue_checkout(self):

        self.find_element(self.locator['checkout']).click()
        time.sleep(3)
        return page.Summary_page(self._driver)

