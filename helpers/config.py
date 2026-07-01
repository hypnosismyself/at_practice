import configparser
import inspect
from pathlib import Path

from selenium.webdriver.chrome.options import Options


class Config:
    """Конфигуратор для тестов"""

    def __init__(self):
        self.__config = configparser.ConfigParser()
        self.__options = Options()
        self.__load_config()

    def get(self, key: str):
        """Получить опцию общего конфига"""
        return self.__config['general'][key]

    def enable_browser_options(self):
        """
        Прокинуть опции из конфига в браузер
        :return Options: объект опций
        """
        self.__options.page_load_strategy = self.__config['custom']['page_load_strategy']
        if self.__config['custom']['headless'] == 'true':
            self.__options.add_argument('--headless')

        return self.__options

    def __load_config(self):
        # Находим первый фрейм, который не является этим файлом (config.py)
        stack = inspect.stack()
        caller_frame = None
        for frame_info in stack:
            # Сравниваем путь файла с текущим (__file__)
            if frame_info.filename != __file__:
                caller_frame = frame_info
                break

        if caller_frame is None:
            # fallback – текущая рабочая директория
            caller_dir = Path.cwd()
        else:
            caller_dir = Path(caller_frame.filename).parent

        config_path = self._find_config(caller_dir)
        if not config_path:
            raise FileNotFoundError(
                f"config.ini не найден ни в {caller_dir}, ни в родительских папках"
            )
        self.__config.read(config_path)

    def _find_config(self, start_dir: Path) -> Path | None:
        """Поднимается вверх по дереву, пока не найдёт config.ini"""
        for parent in [start_dir] + list(start_dir.parents):
            candidate = parent / 'config.ini'
            if candidate.exists():
                return candidate
        return None