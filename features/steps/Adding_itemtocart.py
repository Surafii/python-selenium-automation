from selenium.webdriver.common.by import By
from behave import when, then, given
from selenium.webdriver.common.keys import Keys

ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
CART = (By.ID, 'nav-cart-count')
PRODUCT_RESULT = (By.XPATH, "//div[@data-component-type='a-search-result']//a[.//span[@class='a-price']]")


@when('search for coffee mug')
def input_search(context,):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Coffee mug')


@when('Click the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_RESULT).click()

@when ('Click on add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()

#@then('Verify cart {expected_count} has 1 item')
#def Verify_cart_count(context, expected_count):
   # cart_count = context.driver.find_element(*CART).text
    #assert expected_count == cart_count, f'Expected {expected_count} item but got {cart_count}'

@then('Verify cart has 1 item')
def verify_has_1_item(context):
    actual_item = context.driver.find_element(*CART)
    assert (actual_item) == 1, f'Expected 1 item, but we got {(actual_item)}'
