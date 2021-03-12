from selenium.webdriver.common.by import By
from behave import  when, then

@when('Click Amazon Orders link')
def Click_amazon_orders_link(context):
    context.app.main_page.click_Amazon_orders_link()

@then('verify sign in page is opened')
def verify_sign_in_page_is_opened(context):
    context.app.result_page.verify_sign_in_page_is_opened()












