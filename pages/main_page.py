import driver
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class MainPage(Page):
    MARKET = (By.CSS_SELECTOR, 'a[href="/market-companies"] [class="menu-button-text"]')
    EVENTS = (By.XPATH, '//div[text()="Events"]')
    COMPANIES = (By.CSS_SELECTOR, 'a[class="menu-text-link-leaderboard"][href="/market-companies"]')

    def __init__(self, driver):
        super().__init__(driver)


    def open(self):
        self.open_url('https://soft.reelly.io')

    def open_sign_in(self):
        self.open_url('https://soft.reelly.io/sign-in')

    def click_market(self):
        sleep(3)
        self.find_element(*self.MARKET).click()

    def click_events(self):
        sleep(3)
        self.find_element(*self.EVENTS).click()

    def click_companies(self):
        sleep(3)
        self.find_element(*self.COMPANIES).click()