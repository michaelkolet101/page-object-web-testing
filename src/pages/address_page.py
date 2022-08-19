from playwright.sync_api import sync_playwright
import src.pages.shipping_page as page
import src.pages.base_page as base


class Address_page(base.Base_page):

    def __init__(self, driver: sync_playwright):
        self._driver = driver
        super().__init__(driver)

    locator = {'checkout_btn': '//*[@id="form"]/p/button'}

    def continue_checkout(self):
        standard_checkout = self.find_element(self.locator['checkout_btn'])
        standard_checkout.click()
        return page.Shipping_page(self._driver)
