from selenium.webdriver.common.by import By
from elements.base import BaseElement
from elements.button import Button


class LanguageSwitch(BaseElement):

    def __init__(self, driver, how, locator: str, name: str):
        super().__init__(driver, how, locator, name)
        self.__language_list = ['ru', 'en']
        self.eng_btn = Button(self.driver, By.CSS_SELECTOR, '[data-testid="lang-en"]', 'английский язык')
        self.rus_btn = Button(self.driver, By.CSS_SELECTOR, '[data-testid="lang-ru"]', 'русский язык')

    def __str__(self):
        return f'переключатель языка {self.name}'

    def switch_language(self, language):

        if language not in self.__language_list:
            raise Exception('Выбран несуществующий язык')

        if language == 'en':
            self.eng_btn.click()
            assert 'bg-brand-100' in self.eng_btn.get_attribute('className'), 'Язык не изменился'
        elif language == 'ru':
            self.rus_btn.click()
            assert 'bg-brand-100' in self.rus_btn.get_attribute('className'), 'Язык не изменился'
