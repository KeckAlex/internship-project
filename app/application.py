from pages.base_page import Page
from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.market_page import MarketPage

class Application:
    def __init__(self, driver):
        self.driver = driver

        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.market_page = MarketPage(driver)
