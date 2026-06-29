from pages.BasePage import BasePage
from elements.text import Text
from helpers.by import ByCustom


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'http://localhost:3000/login'
        self.driver = driver
        login = Text(self.driver, ByCustom.DATA_TESTID, 'auth-email-input', 'логин')

    def login(self, email, password):
        self.login.type_in(email)
