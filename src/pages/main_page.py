import time
import src.pages.authntication_page as p
import src.pages.search_reslut_page as res
import src.pages.base_page as base
from playwright.sync_api import sync_playwright



class Main_page(base.Base_page):

    def __init__(self, page: sync_playwright):
        self._page = page
        super().__init__(page)

    locator = {'sign_in': '.login',
               'search': "#search_query_top",
               'submit': ".button-search"
               }

    def Sign_in(self):
        self._page.wait_for_selector(self.locator['sign_in']).click()
        return p.Authnticatuion_page(self._page)

    def search(self, to_find: str):
        search_box = self._page.wait_for_selector(self.locator['search'])
        search_box.fill(to_find)
        search_btn = self._page.wait_for_selector(self.locator['submit'])
        search_btn.click()
        time.sleep(3)
        return res.SearchReslut_page(self._page)
