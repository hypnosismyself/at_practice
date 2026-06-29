import configparser


class Config:

    def __init__(self):
        self.__config = configparser.ConfigParser()
        pass

    def get(self, key: str):
        self.__config.read('config.ini')
        return self.__config['general'][key]
