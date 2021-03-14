from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    CLICK_ORDER = (By.XPATH, "//a[@id='nav-orders']")
    CART_ICON = (By.XPATH, "//span[@class='nav-cart-icon nav-sprite']")



    def open_main_page(self):
        self.open_url("https://www.amazon.com/")

    def input_amazon_search(self, search_query ):
        self.input_text(search_query, *self.SEARCH_FIELD)

    def click_search_amazon(self):
        self.click(*self.SEARCH_ICON)

    def click_Amazon_orders_link(self):
        self.click(*self.CLICK_ORDER)

    def click_on_cart_icon(self):
        self.click(*self.CART_ICON)



