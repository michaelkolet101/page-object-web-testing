from playwright.sync_api import Playwright, sync_playwright, expect
import sys
import pytest
import time
import logging
import src.pages.main_page as main_page

@pytest.fixture
def open_page():
    url = 'http://automationpractice.com/index.php'
    if len(sys.argv) > 1:
        url = sys.argv[1]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        yield main_page.Main_page(page)
        page.close()



TEST_CASES = {"valid": ('michael101@gmail.com', '12345'),
              "not valid 1": ('DanidinTheKing@gmail.com', '12345'),
              "not valid 2": ('banana', '12345'),
              "not valid 3": ('michael101@gmail.com', '123456'),
              "not valid 4": ('michael101@gmail.com', '1234')
              }

def test_login_1(open_page):

    logging.info(TEST_CASES['valid'])
    main_page = open_page
    Authntication_page = main_page.Sign_in()
    MyAccount_page = Authntication_page.login(*TEST_CASES['valid'])
    MyAccount_page.assert_result()

def test_login_2(open_page):
    logging.info(TEST_CASES['not valid 1'])
    main_page = open_page
    Authntication_page = main_page.Sign_in()
    Authntication_page = Authntication_page.login(*TEST_CASES['not valid 1'])
    Authntication_page.Authentication_msg('Authentication failed.')


def test_login_3(open_page):
    logging.info(TEST_CASES['not valid 2'])
    main_page = open_page
    Authntication_page = main_page.Sign_in()
    Authntication_page = Authntication_page.login(*TEST_CASES['not valid 2'])
    Authntication_page.Authentication_msg('Invalid email address')


def test_login_4(open_page):
    main_page = open_page
    Authntication_page = main_page.Sign_in()
    logging.info(TEST_CASES['not valid 3'])
    Authntication_page = Authntication_page.login(*TEST_CASES['not valid 3'])
    Authntication_page.Authentication_msg('Authentication failed.')


def test_login_5(open_page):
    main_page = open_page
    Authntication_page = main_page.Sign_in()
    logging.info(TEST_CASES['not valid 4'])
    Authntication_page = Authntication_page.login(*TEST_CASES['not valid 4'])
    Authntication_page.Authentication_msg('Invalid password.')

def test_login_6(open_page):
    # test to forgot password
    main_page = open_page
    Authntication_page = main_page.Sign_in()
    logging.info('test to forgot password')
    forgot_password_page = Authntication_page.forgot_password()
    forgot_password_page.forgot_result()
