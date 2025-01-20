from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class MainPage(Page):
    MARKET = (By.CSS_SELECTOR, 'a[href="/market-companies"] [class="menu-button-text"]')

    def __init__(self, driver):
        super().__init__(driver)


    def open(self):
        self.open_url('https://soft.reelly.io')

    def open_sign_in(self):
        self.open_url('https://soft.reelly.io/sign-in')

    def click_market(self):
        sleep(3)
        self.find_element(*self.MARKET).click()


