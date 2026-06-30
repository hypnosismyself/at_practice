from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from elements.language_switch import LanguageSwitch
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


WAIT = 5


class BasePage:
    """Базовая страница"""

    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.__wait = WebDriverWait(self.__driver, WAIT)
        self.language_switch = LanguageSwitch(self.__driver, By.CSS_SELECTOR, 'div .absolute', 'свитч языка')
        self.url = ''

    def __str__(self):
        return f'Страница {self.url}'

    @property
    def driver(self):
        return self.__driver

    def open(self):
        """Открыть страницу"""
        self.__driver.get(self.url)

    def switch_language(self, language):
        """
        Поменять язык страницы
        :param language: язык
        """
        self.language_switch.switch_language(language)

    def check_page_changed(self) -> bool:
        """Изменилась ли страница
        :return Bool: True - url изменился / False - не изменился
        """
        return self.__wait.until(EC.url_changes(self.url))
