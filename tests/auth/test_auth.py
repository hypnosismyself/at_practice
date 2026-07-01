from unittest import TestCase

import allure
from selenium import webdriver
from pages.login import LoginPage
from helpers.config import Config


@allure.epic("Магический портал")
@allure.feature("Авторизация")
@allure.story("Успешный вход пользователя")
class LoginTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = Config()
        cls.driver = webdriver.Chrome(options=cls.config.enable_browser_options())
        cls.driver.maximize_window()
        cls.login_page = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @allure.tag('Smoke')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_01_basic_auth(self):
        """Авторизация по логину и паролю"""

        with allure.step('Открываем страницу авторизации'):
            self.login_page.open()

        with allure.step('Авторизуемся по логину и паролю'):
            self.login_page.auth_by_login_and_password(self.config.get('LOGIN'), self.config.get('PASS'))
