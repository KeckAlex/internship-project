from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SignInPage(Page):
    SIGN_IN_TXT = (By.CSS_SELECTOR, "h1[class='form-header']")
    TEXT = 'Sign in'
    EMAIL = 'moniqqaxtr@gmailbrt.com'
    PASSWORD = 'realy@25'
    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    LOG_IN = (By.CSS_SELECTOR, 'a[wized="loginButton"]')

    def verify_sign_in(self):
        self.wait_for_element_appear(*self.SIGN_IN_TXT)
        self.verify_partial_text(self.TEXT, *self.SIGN_IN_TXT)

    def enter_email(self):
        # sleep(3)
        self.wait_for_element_appear(*self.EMAIL_FIELD)
        self.input_text(self.EMAIL, *self.EMAIL_FIELD)

    def enter_password(self):
        self.wait_for_element_appear(*self.PASSWORD_FIELD)
        self.input_text(self.PASSWORD, *self.PASSWORD_FIELD)

    def click_login(self):
        self.find_element(*self.LOG_IN).click()
