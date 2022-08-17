from selenium import webdriver
from selenium.webdriver.common.by import By
import src.pages.base_page as base


class Order_confirmation_page(base.Base_page):

    def __init__(self, driver: webdriver):
        self._driver = driver

    locator = {'box': (By.CLASS_NAME, 'box')}

    def result(self):
        end_msg = self.find_element(*self.locator['box'])
        assert 'Your order on My Store is complete.' in end_msg.text
