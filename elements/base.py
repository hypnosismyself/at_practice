from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaseElement:

    def __init__(self, driver: webdriver, how, locator: str, name: str):
        self.driver = driver
        self.how = how
        self.locator = locator
        self.name = name
        self.__wait = WebDriverWait(self.driver, 10)

    def __str__(self):
        return 'элемент'

    def click(self):
        """Клик по элементу"""
        self.__wait.until(EC.presence_of_element_located((self.how, self.locator))).click()

    def type_in(self, text: str):
        """Ввод текста в элемент"""
        self.__wait.until(EC.presence_of_element_located((self.how, self.locator))).send_keys(text)

    def get_attribute(self, attribute: str):
        """<UNK> <UNK> <UNK> <UNK> <UNK> <UNK> <UNK>"""
        return self.__wait.until(EC.presence_of_element_located((self.how, self.locator))).get_attribute(f'{attribute}')