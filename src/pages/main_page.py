import time
import src.pages.authntication_page as page
import src.pages.search_reslut_page as res
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys


class Main_page:

    def __init__(self, driver: webdriver):
        self._driver = driver

    def Sign_in(self):
        login_btn = self._driver.find_element(By.CLASS_NAME, "login")
        login_btn.click()
        time.sleep(3)
        return page.Authnticatuion_page(self._driver)

    def search(self, to_find: str):
        search_box = self._driver.find_element(By.ID, "search_query_top")
        search_box.send_keys(to_find)
        search_btn = self._driver.find_element(By.NAME, "submit_search")
        search_btn.click()
        return res.SearchReslut_page(self._driver)
