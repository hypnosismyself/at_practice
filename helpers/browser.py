from selenium.webdriver.chrome.webdriver import WebDriver


class Browser:

    def __init__(self, driver: WebDriver):
        self.driver = driver
