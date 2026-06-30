from unittest import TestCase
from selenium import webdriver
from pages.login import LoginPage
from helpers.config import Config


class LoginTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = Config()
        cls.driver = webdriver.Chrome(options=cls.config.enable_browser_options())
        cls.driver.maximize_window()
        cls.login_page = LoginPage(cls.driver)
        cls.login_page.open()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_basic_auth(self):
        self.login_page.auth_by_login_and_password(self.config.get('LOGIN'), self.config.get('PASS'))
