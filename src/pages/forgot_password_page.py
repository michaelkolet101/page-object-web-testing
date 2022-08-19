import time
import src.pages.base_page as base
from selenium import webdriver
from selenium.webdriver.common.by import By


class Forgot_password(base.Base_page):

    def __init__(self, driver: webdriver):
        self._driver = driver
        super().__init__(driver)

    locator = {'page_subheading': (By.TAG_NAME, 'h1'),
               'email_box': (By.ID, 'email'),
               'submit': (By.CLASS_NAME, 'submit'),
               'button': (By.TAG_NAME, 'button'),
               'success': (By.CLASS_NAME, 'alert-success')
               }

    def forgot_result(self):

        page_subheading = self.find_element(*self.locator['page_subheading'])
        assert 'FORGOT YOUR PASSWORD?' in page_subheading.text

        email_box = self.find_element(*self.locator['email_box'])
        email_box.send_keys('michael101@gmail.com')

        sub = self.find_element(*self.locator['submit'])
        button = sub.find_element(*self.locator['button'])
        button.click()
        time.sleep(2)

        success = self.find_element(*self.locator['alert-success'])
        assert 'A confirmation email has been sent to your address:' in success.text
        assert 'michael101@gmail.com' in success.text
        self._driver.quit()
