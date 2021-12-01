from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    MESSAGE_BASKET_IS_EMPTY = (By.XPATH, "//*[contains(text(),'Your basket is empty')]")
    ITEM_IN_BASKET = (By.CSS_SELECTOR, "div.basket-items")

class LoginPageLocators():
    LOGIN_FORM_EMAIL_ADDRESS = (By.CSS_SELECTOR, "input#id_login-username")
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, "input#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary[name='login_submit']")

    REGISTER_FORM_EMAIL_ADRESS = (By.CSS_SELECTOR, "input#id_registration-email")
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password1")
    REGISTER_FORM_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color:nth-child(2)")    
    MESSAGE_PRODUCT_SUCCESSFULLY_ADDED = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")

    #