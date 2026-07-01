import allure
from pages.base import BasePage
from elements.button import Button
from elements.text import Text
from helpers.by import ByCustom


class LoginPage(BasePage):
    """Страница login"""

    def __init__(self, driver):
        super().__init__(driver)
        self.__driver = driver
        self.url = 'http://localhost:3000/login'

        self.login_txt = Text(self.__driver, ByCustom.DATA_TESTID, 'auth-email-input', 'логин')
        self.password_txt = Text(self.__driver, ByCustom.DATA_TESTID, 'auth-password-input', 'пароль')
        self.login_btn = Button(self.__driver, ByCustom.DATA_TESTID, 'auth-login-btn', 'Авторизоваться')

    @allure.step('Авторизуемся по логину и паролю')
    def auth_by_login_and_password(self, email, password):
        """
        Авторизоваться по логину и паролю
        :param email: логин
        :param password: пароль
        """
        self.login_txt.type_in(email)
        assert self.login_txt.value == email, 'Логин не введен'
        self.password_txt.type_in(password)
        assert self.password_txt.value == password, 'Пароль не введен'
        self.login_btn.click()
        assert self.check_page_changed(), 'Не вышли из окна авторизации'
