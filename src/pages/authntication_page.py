import time
import src.pages.base_page as base
import src.pages.my_account_page as page
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By

class Authnticatuion_page(base.Base_page):

    def __init__(self, driver: webdriver):
        self._driver = driver
        self._mail = ""
        self._passwrd = ""

    locator = {'email': (By.ID, "email"),
               'passwd': (By.ID, "passwd"),
               'SubmitLogin': (By.ID, "SubmitLogin")
               }

    def login(self, email: str, passwd: str):
        self._mail = email
        self._passwrd = passwd
        self.fill_mail()
        self.fill_passwd()
        self.click_submit()
        time.sleep(3)
        return page.MyAccount_page(self._driver)

    def fill_mail(self):
        email_box = self.find_element(*self.locator['email'])
        email_box.send_keys(self._mail)

    def fill_passwd(self):
        password_box = self.find_element(*self.locator["passwd"])
        password_box.send_keys(self._passwrd)

    def click_submit(self):
        submit = self.find_element(*self.locator["SubmitLogin"])
        submit.click()
