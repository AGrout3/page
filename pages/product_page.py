from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    def should_be_promo_url(self):
        assert "?promo=" in self.browser.current_url, "Promo is not present"
    
    def should_be_product_page(self):
        self.should_be_add_to_basket_button()
        self.should_be_product_name()
        self.should_be_product_price()    

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "There's no add to basket button"

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "There's no product name"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "There's no product price"

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_messages(self):
        self.should_be_message_about_adding()
        self.should_be_message_about_basket_total()
        self.should_be_product_name_in_adding_message()
        self.should_be_same_product_and_basket_total()
    
    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_SUCCESSFULLY_ADDED), "There is no message of adding product to basket"

    def should_be_message_about_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), "There is no basket total message"

    def should_be_product_name_in_adding_message(self):
        product_name_main = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name_main == self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_SUCCESSFULLY_ADDED).text, "Name of added product was not found in message of adding product to basket"

    def should_be_same_product_and_basket_total(self):
        product_price_main = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price_main == ((self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL)).text), "Basket total is not equal to added product price"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_SUCCESSFULLY_ADDED), "Success message is presented, but should not be"

    def should_dissapear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_PRODUCT_SUCCESSFULLY_ADDED), "Success message is presented, but should not be"
        
        #