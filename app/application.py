from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.search_page import SearchPage
from pages.landing_page import LandingPage
from pages.header_page import HeaderPage

class Application:
    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.landing_page = LandingPage(self.driver)
        self.header_page = HeaderPage(self.driver)