from pages.main_page import MainPage
from pages.result_page import ResultPage


class Application:


    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.result_page =ResultPage(self.driver)
