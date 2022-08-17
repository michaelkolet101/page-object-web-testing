import src.pages.main_page as page

import pytest
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys
# my deatls
# michael101@gmail.com
# 12345

mail = 'michael101@gmail.com'
password = '12345'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrom_driver_path ='/home/michael/seleln/chromedriver'


def test_set_up():
    driver = webdriver.Chrome(chrom_driver_path, chrome_options=chrome_options)
    driver.maximize_window()
    driver.get('http://automationpractice.com/index.php')
    return page.Main_page(driver)


def test_buy_summer():
    main_page = test_set_up()
    Authntication_page = main_page.Sign_in()
    MyAccount_page = Authntication_page.login(mail, password)
    main_page = MyAccount_page.home()
    search_reslut_page = main_page.search("summer")
    cheap_dress_page = search_reslut_page.get_cheap_dress()
    buy_dress_page = cheap_dress_page.buy_the_dress()
    summary_page = buy_dress_page.continue_checkout()
    address_page = summary_page.continue_checkout()
    shipping_page = address_page.continue_checkout()
    payment_page = shipping_page.continue_checkout()
    payment_confirmation_page = payment_page.pay()
    order_confirmation_page = payment_confirmation_page.confirm()
    order_confirmation_page.result()

