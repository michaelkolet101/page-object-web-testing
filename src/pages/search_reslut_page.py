from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import src.pages.cheap_dress_page as page

class SearchReslut_page:

    def __init__(self, driver: webdriver):
        self._driver = driver

    def find_the_min_price(self):
        product_list = self._driver.find_element(By.CLASS_NAME, "product_list")
        product_containers = product_list.find_elements(By.CLASS_NAME, "product-container")
        list_price = []
        minimum_price = 0
        for product_container in product_containers:
            right_block = product_container.find_element(By.CLASS_NAME, "right-block")
            price = right_block.find_element(By.CLASS_NAME, "product-price").text
            list_price.append((price[1::]))
            minimum_price = min(list_price)
        return minimum_price

    def get_cheap_dress(self):
        minimum_price = self.find_the_min_price()
        product_list = self._driver.find_element(By.CLASS_NAME, "product_list")
        product_containers = product_list.find_elements(By.CLASS_NAME, "product-container")
        for product_container in product_containers:
            right_block = product_container.find_element(By.CLASS_NAME, "right-block")
            price = right_block.find_element(By.CLASS_NAME, "product-price").text
            p = float(price[1::])
            if (p == float(minimum_price)):
                left_block = product_container.find_element(By.CLASS_NAME, 'left-block')
                left_block.click()
                break

        time.sleep(3)
        return page.Cheap_dress_page(self._driver)
