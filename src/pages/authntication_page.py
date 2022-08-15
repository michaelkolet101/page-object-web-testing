import time
import src.pages.my_account_page as page
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By

class Authnticatuion_page:


    def __init__(self, driver: webdriver):
        self._driver = driver
        self._mail = ""
        self._passwrd = ""

    def login(self, email: str, passwd: str):
        self._mail = email
        self._passwrd = passwd
        self.fill_mail()
        self.fill_passwd()
        self.click_submit()
        time.sleep(3)
        return page.MyAccount_page(self._driver)

    def fill_mail(self):
        email_box = self._driver.find_element(By.ID, "email")
        email_box.send_keys(self._mail)

    def fill_passwd(self):
        password_box = self._driver.find_element(By.ID, "passwd")
        password_box.send_keys(self._passwrd)

    def click_submit(self):
        submit = self._driver.find_element(By.ID, "SubmitLogin")
        submit.click()
