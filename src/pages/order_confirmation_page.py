from playwright.sync_api import sync_playwright
import src.pages.base_page as base


class Order_confirmation_page(base.Base_page):

    def __init__(self, driver: sync_playwright):
        self._driver = driver
        super().__init__(driver)

    locator = {'box': '.box'}

    def result(self):
        end_msg = self.wait_element(self.locator['box'])
        assert 'Your order on My Store is complete.' in end_msg.text
