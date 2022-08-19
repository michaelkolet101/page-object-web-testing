import time
import src.pages.forgot_password_page as frgot
import src.pages.base_page as base
import src.pages.my_account_page as p
import logging
from playwright.sync_api import sync_playwright


class Authnticatuion_page(base.Base_page):

    def __init__(self, driver: sync_playwright):
        self._driver = driver
        self._mail = ""
        self._passwrd = ""

    locator = {'email': 'id=email',
               'passwd': 'id=passwd',
               'SubmitLogin': 'id=SubmitLogin',
               'alert-danger': ('By.CLASS_NAME', 'alert-danger'),
               'lost_password': ('By.CLASS_NAME', 'lost_password'),
               'link': ('By.TAG_NAME', 'a')
               }

    def login(self, email: str, passwd: str):
        self._mail = email
        self._passwrd = passwd
        self.fill_mail()
        self.fill_passwd()
        self.click_submit()
        time.sleep(3)
        return p.MyAccount_page(self._driver)

    def fill_mail(self):
        email_box = self._driver.locator(self.locator['email'])
        email_box.fill(self._mail)

    def fill_passwd(self):
        password_box = self._driver.locator(self.locator["passwd"])
        password_box.fill(self._passwrd)

    def click_submit(self):
        submit = self._driver.locator(self.locator["SubmitLogin"])
        submit.click()
    #
    # def Authentication_msg(self, msg: str):
    #     res = self._driver.locator(self.locator['alert-danger'])
    #     assert msg in res.text
    #     logging.info(res.text)
    #     time.sleep(3)
    #     self._driver.quit()
    #
    # def forgot_password(self):
    #     lost_password = self._driver.locator(self.locator['lost_password'])
    #     link = lost_password.locator(self.locator['link'])
    #     link.click()
    #     time.sleep(1)
    #     return frgot.Forgot_password(self._driver)
