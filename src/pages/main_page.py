import time
import src.pages.authntication_page as page
import src.pages.search_reslut_page as res
import src.pages.base_page as base
from playwright.sync_api import sync_playwright



class Main_page(base.Base_page):

    def __init__(self, driver: sync_playwright):
        self._driver = driver

    locator = {'sign_in': '.login',
               'search': "#search_query_top",
               'submit': ".button-search"
               }

    def Sign_in(self):
        time.sleep(3)
        login_btn = self.find_element(self.locator['sign_in'])
        login_btn.click()
        time.sleep(3)
        return page.Authnticatuion_page(self._driver)

    def search(self, to_find: str):
        search_box = self._driver.wait_for_selector(self.locator['search'])
        search_box.fill(to_find)
        search_btn = self._driver.wait_for_selector(self.locator['submit'])
        search_btn.click()
        return res.SearchReslut_page(self._driver)
