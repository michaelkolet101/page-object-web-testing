from selenium import webdriver
from selenium.webdriver.common.by import By
import src.pages.summary_page as page
import src.pages.base_page as base
import time


class Buy_dress_page(base.Base_page):

    def __init__(self, driver: webdriver):
        self._driver = driver

    locator = {'layer_cart': (By.CLASS_NAME, "layer_cart_cart"),
               'button-container': (By.CLASS_NAME, "button-container"),
               'button': (By.CLASS_NAME, "button-medium")
               }
    def continue_checkout(self):
        layer_cart_cart = self.find_element(*self.locator['layer_cart'])
        button_container = layer_cart_cart.find_element(*self.locator['button-container'])
        btn = button_container.find_element(*self.locator['button'])
        btn.click()
        time.sleep(5)

        return page.Summary_page(self._driver)

