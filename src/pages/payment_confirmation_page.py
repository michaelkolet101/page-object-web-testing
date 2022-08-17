import src.pages.base_page as base
from selenium import webdriver
from selenium.webdriver.common.by import By
import src.pages.order_confirmation_page as page


class Payment_confirmation(base.Base_page):

    def __init__(self, driver: webdriver):
        self._driver = driver

    locator = {'cart': (By.ID, 'cart_navigation'),
               'button': (By.CLASS_NAME, 'button-medium')
               }

    def confirm(self):
        cart_navigation = self.find_element(*self.locator['cart'])
        confirm = cart_navigation.find_element(*self.locator['button'])
        confirm.click()
        return page.Order_confirmation_page(self._driver)
