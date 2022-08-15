from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import src.pages.summary_page as page

class Buy_dress_page:

    def __init__(self, driver: webdriver):
        self._driver = driver

    def buy_the_dress(self):
        layer_cart_cart = self._driver.find_element(By.CLASS_NAME, "layer_cart_cart")
        button_container = layer_cart_cart.find_element(By.CLASS_NAME, "button-container")
        btn = button_container.find_element(By.CLASS_NAME, "button-medium")
        btn.click()
        time.sleep(3)
        return page.Summary_page(self._driver)

