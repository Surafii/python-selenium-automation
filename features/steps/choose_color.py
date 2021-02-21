from selenium.webdriver.common.by import By
from behave import when, then, given
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name  li")
SELECTED_COLOR = (By.CSS_SELECTOR, "#variation_color_name  .selection")



@given('Open Amazon Jeans B07BJKRR25 page')
def open_amazon_jeans_B07BJKRR25_page(context):
    context.driver.get('https://www.amazon.com/gp/product/B07BJKRR25/')




@then('Verify user can click through colors')
def  user_can_click_through_colors(context):
    expected_colors = ['Black', 'Blue Overdyed', 'Dark Vintage', 'Dark Wash', 'Indigo Wash', 'Light Vintage', 'Light Wash',
                                                                                                              'Medium Vintage', 'Medium Wash', 'Rinse', 'Rinsed Vintage', 'Vintage Light Wash', 'Washed Black']
    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for i in range(len(colors)):
        colors[i].click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        assert expected_colors[i] == selected_color, f'Expected {expected_colors[i]} but got {selected_color}'