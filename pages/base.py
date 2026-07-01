from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from elements.language_switch import LanguageSwitch
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure


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
        with allure.step('Открываем страницу браузера'):
            self.__driver.get(self.url)

    def switch_language(self, language):
        """
        Поменять язык страницы
        :param language: язык
        """
        with allure.step(f'Меняем язык на {language}'):
            self.language_switch.switch_language(language)

    def check_page_changed(self) -> bool:
        """Изменилась ли страница
        :return bool: True - url изменился / False - не изменился
        """
        with allure.step(f'Проверяем изменение урла'):
            return self.__wait.until(EC.url_changes(self.url))
