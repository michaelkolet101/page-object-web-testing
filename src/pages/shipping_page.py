import src.pages.base_page as base
import src.pages.payment_page as page
from playwright.sync_api import sync_playwright
import time


class Shipping_page(base.Base_page):
    def __init__(self, driver: sync_playwright):
        self._driver = driver
        super().__init__(driver)

    locator = {'check_box': "#cgv",
               'btn_contine': '//*[@id="form"]/p/button'
               }

    def chack(self):
        chack_box = self.wait_element(self.locator['check_box'])
        time.sleep(3)
        chack_box.click()

    def continue_checkout(self):
        self.chack()
        standard_checkout = self.find_element(self.locator['btn_contine'])
        standard_checkout.click()
        return page.Payment_page(self._driver)


