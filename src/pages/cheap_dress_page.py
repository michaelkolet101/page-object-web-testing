from selenium import webdriver
from selenium.webdriver.common.by import By
import src.pages.base_page as base
import src.pages.buy_dress_page as page
import time


class Cheap_dress_page(base.Base_page):

    def __init__(self, driver: webdriver):
        self._driver = driver

    locator = {'columns-container': (By.CLASS_NAME, 'columns-container'),
               'buy_block': (By.ID, 'buy_block'),
               'Submit': (By.NAME, 'Submit')
               }

    def buy_the_dress(self):
        columns_container = self.find_element(*self.locator['columns-container'])
        buy_block = columns_container.find_element(*self.locator['buy_block'])
        submit = buy_block.find_element(*self.locator['Submit'])
        submit.click()
        time.sleep(5)
        return page.Buy_dress_page(self._driver)