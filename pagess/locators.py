from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
    EMAIL_INPUT = (By.ID, "id_registration-email")
    PASSWORD_INPUT = (By.ID, "id_registration-password1")
    PASSWORD_INPUT_CONFIRM = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, 'registration_submit')

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, 'div.alertinner > strong')
    BASKET_TOTAL = (By.CSS_SELECTOR, 'div.alertinner > p > strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main > h1')
    BASKET_LINK = (By.CSS_SELECTOR, 'span.btn-group > a.btn-default')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_main > p')

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, 'div.content > div#content_inner > p')
    BASKET_PRODUCTS = (By.CSS_SELECTOR, 'div.content > div#content_inner > div')
    BASKET_LINK = (By.CSS_SELECTOR, 'span.btn-group > a.btn-default')

