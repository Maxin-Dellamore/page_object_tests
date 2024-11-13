from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def should_be_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS), \
            "Products is not presented, but it should be"

    def should_not_be_items(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Products is presented, but should not be"