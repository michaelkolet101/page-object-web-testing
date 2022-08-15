from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import src.pages.buy_dress_page as page

class Cheap_dress_page:

    def __init__(self, driver: webdriver):
        self._driver = driver

    def buy_the_dress(self):
        columns_container = self._driver.find_element(By.CLASS_NAME, 'columns-container')
        buy_block = columns_container.find_element(By.ID, 'buy_block')
        submit = buy_block.find_element(By.NAME, 'Submit')
        submit.click()
        time.sleep(3)
        return page.Buy_dress_page(self._driver)