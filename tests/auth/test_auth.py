from unittest import TestCase
import allure
import pytest
import requests
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

    @pytest.mark.acceptance
    def test_01_basic_auth(self):
        """Авторизация по логину и паролю"""
        with allure.step('Открываем страницу авторизации'):
            self.login_page.open()

        with allure.step('Авторизуемся по логину и паролю'):
            self.login_page.auth_by_login_and_password(self.config.get('LOGIN'), self.config.get('PASS'))

    @pytest.mark.smoke
    def test_02_fast_auth(self):
        """Авторизация по быстрой кнопке"""
        with allure.step('Авторизуемся кнопкой быстрой авторизации'):
            self.login_page.fast_auth(self.config.get('ROLE'))

    def tearDown(self):
        with allure.step('Чистим Local storage'):
            self.driver.execute_script('localStorage.clear();')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
