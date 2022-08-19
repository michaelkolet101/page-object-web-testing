import src.pages.base_page as base
import src.pages.order_confirmation_page as page
from playwright.sync_api import sync_playwright

class Payment_confirmation(base.Base_page):

    def __init__(self, driver: sync_playwright):
        self._driver = driver
        super().__init__(driver)


    locator = {'cart': '#cart_navigation',
               'button': '.button-medium'
               }

    def confirm(self):
        cart_navigation = self.wait_element(self.locator['cart'])
        confirm = cart_navigation.wait_for_selector(self.locator['button'])
        confirm.click()

        return page.Order_confirmation_page(self._driver)
