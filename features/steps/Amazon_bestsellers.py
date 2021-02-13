from selenium.webdriver.common.by import By
from behave import when, then

Amazon_bestseller = (By.ID, 'zg-header')

@given('open amazon best seller page')
def open_amazon_best_seller_page(context):
    context.driver.get('https://www.amazon.com/bestsellers/')


@then('Verify if there are 5 links')
def Verify_5_links(context):
    context.driver.find_elements(*Amazon_bestseller)
    actual_links = context.driver.find_elements(*Amazon_bestseller)
    assert len(actual_links) == 5, f'Expected 5 links, but we got {len(actual_links)}'
