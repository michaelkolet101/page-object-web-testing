
import sys
import pytest
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import src.pages.main_page as main_page

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrom_driver_path = '/home/michael/seleln/chromedriver'



class Test_login:

    def __init__(self):
        self._driver = webdriver.Chrome(chrom_driver_path, chrome_options=chrome_options)
        self._driver.maximize_window()
        url = 'http://automationpractice.com/index.php'
        if len(sys.argv) > 1:
            url = sys.argv[1]

        self._driver.get(url)

    def test_set_up(self):
        return main_page.Main_page(self._driver)

    TEST_CASES = {"valid": ('michael101@gmail.com', '12345'),
                  "not valid 1": ('DanidinTheKing@gmail.com', '12345'),
                  "not valid 2": ('banana', '12345'),
                  "not valid 3": ('michael101@gmail.com', '123456'),
                  "not valid 4": ('michael101@gmail.com', '1234')
                  }

    def login_to_acoount(self, uesr_info: tuple):
        """
        :param driver:
        :param uesr_info:
        :return: NAN
        """
        email = uesr_info[0]
        passwd = uesr_info[1]

        login_btn = self._driver.find_element(By.CLASS_NAME, "login")
        login_btn.click()
        time.sleep(2)

        email_box = self._driver.find_element(By.ID, "email")
        password_box = self._driver.find_element(By.ID, "passwd")

        email_box.send_keys(email)
        password_box.send_keys(passwd)

        submit = self._driver.find_element(By.ID, "SubmitLogin")
        submit.click()


    def test_login_1(self):

        logging.info(self.TEST_CASES['valid'])
        main_page = self.test_set_up()
        Authntication_page = main_page.Sign_in()
        MyAccount_page = Authntication_page.login(*self.TEST_CASES['valid'])
        MyAccount_page.assert_result()

    def test_login_2(self):
        logging.info(self.TEST_CASES['not valid 1'])
        main_page = self.test_set_up()
        Authntication_page = main_page.Sign_in()
        Authntication_page = Authntication_page.login(*self.TEST_CASES['not valid 1'])
        Authntication_page.Authentication_msg('Authentication failed.')


    def test_login_3(self):
        logging.info(self.TEST_CASES['not valid 2'])
        main_page = self.test_set_up()
        Authntication_page = main_page.Sign_in()
        Authntication_page = Authntication_page.login(*self.TEST_CASES['not valid 2'])
        Authntication_page.Authentication_msg('Invalid email address')


    def test_login_4(self):
        main_page = self.test_set_up()
        Authntication_page = main_page.Sign_in()
        logging.info(self.TEST_CASES['not valid 3'])
        Authntication_page = Authntication_page.login(*self.TEST_CASES['not valid 3'])
        Authntication_page.Authentication_msg('Authentication failed.')


    def test_login_5(self):
        main_page = self.test_set_up()
        Authntication_page = main_page.Sign_in()
        logging.info(self.TEST_CASES['not valid 4'])
        Authntication_page = Authntication_page.login(*self.TEST_CASES['not valid 4'])
        Authntication_page.Authentication_msg('Invalid password.')

    def test_login_6(self):
        # test to forgot password
        main_page = self.test_set_up()
        Authntication_page = main_page.Sign_in()
        logging.info('test to forgot password')
        forgot_password_page = Authntication_page.forgot_password()
        forgot_password_page.forgot_result()
