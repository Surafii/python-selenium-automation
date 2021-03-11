from selenium.webdriver.common.by import By
from pages.base_page import Page
from behave import when, then, given

@when('Click on cart icon')
def Click_on_cart_icon(context):
    context.app.main_page.click_on_cart_icon()

@then('Verify Your Shopping Cart is empty')
def Verify_Your_Shopping_Cart_is_empty(context):
    context.app.result_page.Verify_Your_Shopping_Cart_is_empty()