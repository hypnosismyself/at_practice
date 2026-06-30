import configparser
from selenium.webdriver.chrome.options import Options


class Config:

    def __init__(self):
        self.__config = configparser.ConfigParser()
        self.__options = Options()
        self.__config.read('config.ini')

    def get(self, key: str):
        return self.__config['general'][key]

    def enable_browser_settings(self):
        self.__options.page_load_strategy = self.__config['browser']['page_load_strategy']
        if self.__config['browser']['headless'] == 'true':
            self.__options.add_argument('--headless')

        return self.__options
