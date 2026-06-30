from elements.button import Button
from pages.BasePage import BasePage
from elements.text import Text
from helpers.by import ByCustom


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'http://localhost:3000/login'
        self.driver = driver
        self.login_txt = Text(self.driver, ByCustom.DATA_TESTID, 'auth-email-input', 'логин')
        self.password_txt = Text(self.driver, ByCustom.DATA_TESTID, 'auth-password-input', 'пароль')
        self.login_btn = Button(self.driver, ByCustom.DATA_TESTID, 'auth-login-btn', 'Авторизоваться')

    def login(self, email, password):
        self.login_txt.type_in(email)
        self.password_txt.type_in(password)
        self.login_btn.click()
