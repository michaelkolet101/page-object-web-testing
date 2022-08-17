from selenium import webdriver
from selenium.webdriver.common.by import By
import src.pages.base_page as base
import src.pages.cheap_dress_page as page

class SearchReslut_page(base.Base_page):

    def __init__(self, driver: webdriver):
        self._driver = driver

    locator = {'product list': ".product_list",
               'product': ".product-container",
               'right-block': (By.CLASS_NAME, "right-block"),
               'price': (By.CLASS_NAME, "product-price"),
               'left-block': (By.CLASS_NAME, 'left-block')
               }

    def find_the_min_price(self):
        product_list = self.find_element(*self.locator['product list'])
        product_containers = product_list.find_elements(*self.locator['product'])
        list_price = []
        minimum_price = 0
        for product_container in product_containers:
            right_block = product_container.find_element(*self.locator['right-block'])
            price = right_block.find_element(*self.locator['price']).text
            list_price.append((price[1::]))
            minimum_price = min(list_price)
        return minimum_price

    def get_cheap_dress(self):
        minimum_price = self.find_the_min_price()
        product_list = self.find_element(*self.locator['product list'])
        product_containers = product_list.find_elements(*self.locator['product'])
        for product_container in product_containers:
            right_block = product_container.find_element(*self.locator['right-block'])
            price = right_block.find_element(*self.locator['price']).text
            p = float(price[1::])
            if (p == float(minimum_price)):
                left_block = product_container.find_element(*self.locator['left-block'])
                left_block.click()
                break

        return page.Cheap_dress_page(self._driver)
