from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaseElement:

    def __init__(self, driver: webdriver, how, locator: str, name: str, wait=5):
        self.driver = driver
        from helpers.by import ByCustom
        if how == ByCustom.DATA_TESTID:
            self.how, self.locator  = By.CSS_SELECTOR, f'[data-testid="{locator}"]'
        else:
            self.how, self.locator = how, locator
        self.name = name
        self.__wait = WebDriverWait(self.driver, wait)

    def __str__(self):
        return 'элемент'

    def click(self):
        """Клик по элементу"""
        self.__wait.until(EC.element_to_be_clickable((self.how, self.locator))).click()

    def type_in(self, text: str):
        """Ввод текста в элемент"""
        self.__wait.until(EC.presence_of_element_located((self.how, self.locator))).send_keys(text)

    def get_attribute(self, attribute: str):
        """Собрать аттрибут"""
        return self.__wait.until(EC.presence_of_element_located((self.how, self.locator))).get_attribute(f'{attribute}')

    def has_class(self, classname: str):
        """Есть класс"""
        element = self.__wait.until(EC.presence_of_element_located((self.how, self.locator)))
        return classname in element.get_attribute('className')