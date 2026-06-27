from selenium.webdriver.chrome import webdriver

from elements.base import BaseElement


class Button(BaseElement):

    def __init__(self, driver: webdriver, how, locator: str, name: str):
        super().__init__(driver, how, locator, name)

    def __str__(self):
        return f'кнопка {self.name}'
