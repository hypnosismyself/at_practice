from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from elements.language_switch import LanguageSwitch


class BasePage:

    url = ''

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.language_switch = LanguageSwitch(self.driver, By.CSS_SELECTOR, 'div .absolute', 'свитч языка')

    def open(self):
        """Открыть страницу"""
        self.driver.get(self.url)

    def switch_language(self, language):
        """
        Поменять язык страницы
        :param language: язык из __language_list
        """
        self.language_switch.switch_language(language)
