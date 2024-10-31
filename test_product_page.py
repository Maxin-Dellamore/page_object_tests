from pagess.product_page import ProductPage
import pytest

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    product_name = page.check_product_name()
    product_price = page.check_product_price()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_name(product_name)
    page.should_be_basket_total(product_price)