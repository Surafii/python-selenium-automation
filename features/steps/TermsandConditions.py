from selenium.webdriver.common.by import By
from behave import when, then, given
from selenium.webdriver.support import expected_conditions as EC

APP_LINK = (By.XPATH, "//a[@href= 'https://www.amazon.com/gp/feature.html?docId=1000625601']")
URL = 'https://www.amazon.com/gp/feature'


@given('Open Amazon Terms_and_Conditions page')
def Open_Amazon_Terms_and_Conditions_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html?nodeId=GLSBYFE9MGKKQXXM')

#@when('Store original windows')
#def store_windows(context):
    #original_window = context.driver.current_window_handle

@when('Click on Amazon applications link')
def Click_img(context):
     context.driver.find_element(*APP_LINK).click()

#@when('Switch to the newly opened window')
#def Switch_to_new_window(context):
    #context.driver.wait.until(EC.new_window_is_opened)
    #print(context.driver.window_handles)
    #context.driver.switch_to.window(context.driver.window_handles[1])

#@then('Verify Amazon  page is opened')
#def Verify_Amazon_page_is_opened(context):
    #Expected_url = 'https://www.amazon.com/gp/feature'
    #assert 'https://www.amazon.com/gp/feature' in URL.title

#@then('user can close new window and switch back to original window')
#def close_old_switch_to_new_window(context):
    #context.driver.switch_to.window(context.driver.window_handles[1])
    #context.driver.close()












