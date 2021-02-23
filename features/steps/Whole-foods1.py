from selenium.webdriver.common.by import By
from behave import when, then, given
from selenium.webdriver.support import expected_conditions as EC

PRODUCTS = (By.XPATH, "//div[@class='a-section a-padding-none a-text-center wfm-desktop-section-size']\
//span[@class='a-size-small a-color-tertiary wfm-sales-item-card__regular-price']")

PRODUCT_NAME = (By.XPATH, "//span[@class='a-size-medium wfm-sales-item-card__product-name a-text-bold']")

@given('open amazon wholefoods page')
def open_amazon_wholefoods_page(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')

@then('Verify customer can see all the regular prices')
def Verify_customer_can_see_all_the_regular_prices(context):
    product_element = context.driver.find_elements(*PRODUCTS)
    for e in product_element:
        assert 'Regular' in e.text, f'Error'
        product_name = e.find_element(*PRODUCT_NAME).text
        assert product_name , f'Error'