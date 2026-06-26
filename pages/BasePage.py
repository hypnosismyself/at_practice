from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    url = ''
    __language_list = ['ru', 'en']

    eng_btn = (By.CSS_SELECTOR, '[data-testid="lang-en"]')
    rus_btn = (By.CSS_SELECTOR, '[data-testid="lang-ru"]')

    def open(self):
        """Открыть страницу"""
        self.driver.get(self.url)

    def switch_language_to(self, language):
        """
        Поменять язык страницы
        :param language: язык из __language_list
        """
        if language not in self.__language_list:
            raise Exception('Выбран несуществующий язык')

        if language == 'en':
            btn = self.driver.find_element(*self.eng_btn)
            btn.click()
            assert 'hover:text-gray-600' in btn.get_attribute('className'), 'Язык не изменился'
        elif language == 'ru':
            btn = self.driver.find_element(*self.rus_btn)
            btn.click()
            assert 'hover:text-gray-600' in btn.get_attribute('className'), 'Язык не изменился'
