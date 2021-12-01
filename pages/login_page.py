from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.browser.current_url, "Login link is missing"
            
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_EMAIL_ADDRESS), "Login form email address field is missing"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_PASSWORD), "Login form password field is missing"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is missing"
            
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_EMAIL_ADRESS), "Register form email address field does not exist"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_PASSWORD), "Register form password field does not exist"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_CONFIRM_PASSWORD), "Register form confirm password field is missing"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register button is missing"
                
    def register_new_user(self):
        email_generator = str(time.time()) + "@fakemail.org"
        password = "randompassword"
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL_ADRESS).send_keys(email_generator)        
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
        
        #