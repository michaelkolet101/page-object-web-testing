import logging
import time

from playwright.sync_api import sync_playwright
import src.pages.base_page as base
import src.pages.cheap_dress_page as p


class SearchReslut_page(base.Base_page):

    def __init__(self, driver: sync_playwright):
        self._driver = driver
        super().__init__(driver)

    locator = {
               'product': ".product-container",
               'price': ".product-price",
               'add_to_cart_button': '.ajax_add_to_cart_button'
               }

    def finding_relevant(self) -> dict:
        """
        finding relevant products - and make a Dict[price:product]
        :param open_page:
        :return: dict of products
        """
        product_list = self._driver.query_selector_all(self.locator['product'])
        price_list = {}
        for product in product_list:
            price = product.query_selector(self.locator['price']).text_content().strip()
            logging.info(price)
            # Dict[price:product]
            price_list[price] = product

        return price_list

    def get_cheap_dress(self):
        price_list = self.finding_relevant()
        logging.info(price_list)
        # finding cheap dress
        cheapes = min(price_list.keys())
        price_list[cheapes].click()

        # add to cart
        price_list[cheapes].query_selector(self.locator['add_to_cart_button']).click()
        self._driver.wait_for_timeout(2)

        return p.Cheap_dress_page(self._driver)
