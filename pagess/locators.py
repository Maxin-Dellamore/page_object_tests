from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, 'div.alertinner > strong')
    BASKET_TOTAL = (By.CSS_SELECTOR, 'div.alertinner > p > strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_main > p')

