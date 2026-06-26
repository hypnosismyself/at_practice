import unittest

from selenium import webdriver

from pages.login import LoginPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.login_page = LoginPage(cls.driver)
        cls.login_page.open()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_switch_language(self):
        self.login_page.switch_language_to('en')
