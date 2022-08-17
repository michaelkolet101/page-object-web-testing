import src.pages.base_page as base
import src.pages.payment_page as page
from selenium import webdriver
from selenium.webdriver.common.by import By


class Shipping_page(base.Base_page):
    def __init__(self, driver: webdriver):
        self._driver = driver

    locator = {'chack_box': (By.NAME, 'cgv'),
               'btn_contine': (By.NAME, 'processCarrier')
               }

    def chack(self):
        chack_box = self.find_element(*self.locator['chack_box'])
        chack_box.click()

    def continue_checkout(self):
        self.chack()
        standard_checkout = self.find_element(*self.locator['btn_contine'])
        standard_checkout.click()
        return page.Payment_page(self._driver)


