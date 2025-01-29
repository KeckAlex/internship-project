from selenium.webdriver.common.by import By
from behave import given, when, then

CALEV = (By.CSS_SELECTOR, 'div[class="referrals-text-game"]')

@then('Verify the right {part_url} page opens')
def verify_right_page(context, part_url):
    context.app.market_page.verify_page(part_url)

@then('Verify the proper {part_text} page opens')
def verify_proper_page(context, part_text):
    context.app.market_page.verify_partial_text(part_text, *CALEV)

@then('Click on “Add Company” button')
def open_add_company(context):
    context.app.market_page.add_company_btn()

@then('Verify the buttons "Publish my company" are clickable')
def verify_publish_my_company(context):
    context.app.market_page.verify_buttons()