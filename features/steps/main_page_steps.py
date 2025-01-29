from selenium.webdriver.common.by import By
from behave import given, when, then



@given('Open the main page')
def open_reelly(context):
    context.app.main_page.open()

@given('Open sign in page')
def open_sign_in(context):
    context.app.main_page.open_sign_in()

@then("At the left side menu click on Market")
def click_market(context):
    context.app.main_page.click_market()

@then("On the bottom menu click on Events btn")
def click_events(context):
    context.app.main_page.click_events()

@then("Click on “Companies” btn")
def click_companies(context):
    context.app.main_page.click_companies()