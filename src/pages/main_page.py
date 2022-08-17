import time
import src.pages.authntication_page as page
import src.pages.search_reslut_page as res
import src.pages.base_page as base
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys


class Main_page(base.Base_page):

    def __init__(self, driver: webdriver):
        self._driver = driver

    locator = {'sign_in': (By.CLASS_NAME, 'login'),
               'search': (By.ID, "search_query_top"),
               'submit': (By.NAME, "submit_search")
               }
    # *self.locator['sign_in']
    def Sign_in(self):
        time.sleep(3)
        login_btn = self.find_element(*self.locator['sign_in'])
        login_btn.click()
        time.sleep(3)
        return page.Authnticatuion_page(self._driver)

    def search(self, to_find: str):
        search_box = self._driver.find_element(*self.locator['search'])
        search_box.send_keys(to_find)
        search_btn = self._driver.find_element(*self.locator['submit'])
        search_btn.click()
        return res.SearchReslut_page(self._driver)
