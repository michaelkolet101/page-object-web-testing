import src.pages.main_page as page
from playwright.sync_api import sync_playwright
import src.pages.base_page as base
import time


class MyAccount_page(base.Base_page):
    def __init__(self, driver: sync_playwright):
        self._driver = driver
        super().__init__(driver)

    locator = {'home': '//*[@id="center_column"]/ul/li/a',
               'info-account': '.info-account'
               }

    def home(self):
        btn_home = self.wait_element(self.locator['home'])
        btn_home.click()
        return page.Main_page(self._driver)

    def assert_result(self):
        text = self.find_element(self.locator['info-account'])
        assert 'Welcome to your account' in text.inner_text
        time.sleep(3)
        self._driver.quit()