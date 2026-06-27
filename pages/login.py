from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'http://localhost:3000/login'

    def login(self):
        pass
