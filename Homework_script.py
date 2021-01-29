from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/surafiiabetew/Desktop/Automation/python-selenium-automation/chromedriver')
driver.implicitly_wait(4)
driver.get('https://www.amazon.com/gp/help/customer/display.html')
search_field = driver.find_element(By.ID, 'helpsearch').send_keys('Cancel Order')

search_icon = driver.find_element(By.ID, 'helpsearch').click()

actual_text = driver.find_element(By.XPATH, "//div[@class='help-content']").text
expected_text = 'Cancel Items or Orders'
assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text} '

driver.quit()