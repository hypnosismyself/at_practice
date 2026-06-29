from unittest import TestCase
from selenium import webdriver
from pages.login import LoginPage
from helpers.config import Config


class LoginTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.login_page = LoginPage(cls.driver)
        cls.login_page.open()
        cls.config = Config()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_switch_language(self):
        print(self.config.get('LOGIN'))
        self.login_page.switch_language('en')
