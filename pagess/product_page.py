from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def check_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "It isn't a product name"
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def check_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "It isn't a product price"
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()
        #assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Basket button is not found"

    def should_be_product_name(self, in_basket_product_name):
        basket_product_name = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME).text
        assert in_basket_product_name == basket_product_name, "Product names mismatch"

    def should_be_basket_total(self, in_basket_total):
        busket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert in_basket_total == busket_total, "Product prices mismatch"