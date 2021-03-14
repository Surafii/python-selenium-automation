from selenium.webdriver.common.by import By
from pages.base_page import Page


class ResultPage(Page):
      NEW_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")


      def verify_search_result(self):
        actual_text = self.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
        expected_text = '"Cup"'
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text} '

      def verify_sign_in_page_is_opened(self):
        #assert 'https://www.amazon.com/ap/signin ' in self.driver.current_url, f'Url {self.driver.current_url} does not include https://www.amazon.com/ap/signin'
         actual_text = self.driver.find_element(*self.NEW_TEXT).text
         expected_text = 'Sign-In'
         assert expected_text == actual_text, f'Expected{expected_text}, but got {actual_text}'






      def Verify_Your_Shopping_Cart_is_empty(self):
        actual_text = self.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2").text
        expected_text = 'Your Amazon Cart is empty'
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text} '





