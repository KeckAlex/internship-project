from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Verify Sign in page opened')
def verify_sign_in_page_open(context):
    context.app.sign_in_page.verify_sign_in()


@when('Sign in to account')
def sign_in(context):
    context.app.sign_in_page.enter_email()
    context.app.sign_in_page.enter_password()
    context.app.sign_in_page.click_login()
