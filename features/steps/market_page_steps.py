from behave import given, when, then


@then('Verify the right {part_url} page opens')
def verify_right_page(context, part_url):
    context.app.market_page.verify_page(part_url)

@then('Click on “Add Company” button')
def open_add_company(context):
    context.app.market_page.add_company_btn()

@then('Verify the btn "Publish my company" is clickable')
def verify_publish_my_company(context):
    context.app.market_page.verify_btn()