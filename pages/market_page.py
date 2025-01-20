from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class MarketPage(Page):
    URL = 'market-companies'
    ADD_CO = (By.CSS_SELECTOR, 'a[href="/presentation-for-the-agency"]')
    PUBLISH_BTN_1 = (By.CSS_SELECTOR, '[class="publish-button w-button"]')
    PUBLISH_BTN_2 = (By.CSS_SELECTOR, '[class="publish-button _1 w-button"]')


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verify_page(self, part_url):
        sleep(3)
        self.verify_partial_url(part_url)

    def add_company_btn(self):
        self.find_element(*self.ADD_CO).click()

    def verify_buttons(self):
        self.wait_to_be_clickable(*self.PUBLISH_BTN_1)
        self.wait_to_be_clickable(*self.PUBLISH_BTN_2)