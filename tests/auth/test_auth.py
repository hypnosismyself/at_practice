from unittest import TestCase
import allure
import pytest
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

    def setUp(self):
        with allure.step('Открываем страницу авторизации'):
            self.login_page.open()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.acceptance
    def test_01_basic_auth(self):
        """Авторизация по логину и паролю"""

        with allure.step('Открываем страницу авторизации'):
            self.login_page.open()

        with allure.step('Авторизуемся по логину и паролю'):
            self.login_page.auth_by_login_and_password(self.config.get('LOGIN'), self.config.get('PASS'))

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_02_fast_auth(self):
        """Авторизация по быстрой кнопке"""
        with allure.step('Авторизуемся кнопкой быстрой авторизации'):
            self.login_page.fast_auth(self.config.get('ROLE'))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
