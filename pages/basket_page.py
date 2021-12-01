from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET), "Some products present in basket, but should not be"
        
    def message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY), "There is no 'Basket is empty' message"
