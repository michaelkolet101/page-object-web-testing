import src.pages.main_page as p
import pytest
import time
import logging
import pytest
from playwright.sync_api import sync_playwright

my_user = ["michael101@gmail.com", "12345"]
Test_log = logging.getLogger()

import sys


# my deatls
# michael101@gmail.com
# 12345

mail = 'michael101@gmail.com'
password = '12345'


url = 'http://automationpractice.com/index.php'
if len(sys.argv) > 1:
    url = sys.argv[1]







def test_set_up(page):
    return p.Main_page(page)


def test_buy_summer():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("http://automationpractice.com/index.php")

        main_page = test_set_up(page)
        Authntication_page = main_page.Sign_in()
        MyAccount_page = Authntication_page.login(mail, password)
        main_page = MyAccount_page.home()
        search_reslut_page = main_page.search("summer")
        cheap_dress_page = search_reslut_page.get_cheap_dress()
        buy_dress_page = cheap_dress_page.buy_the_dress()
        summary_page = buy_dress_page.continue_checkout()

        address_page = summary_page.continue_checkout()
        shipping_page = address_page.continue_checkout()
        time.sleep(10)
        payment_page = shipping_page.continue_checkout()
        payment_confirmation_page = payment_page.pay()
        order_confirmation_page = payment_confirmation_page.confirm()
        order_confirmation_page.result()

