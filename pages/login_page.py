from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self,email, password):
        Email_address= self.browser.find_element(*LoginPageLocators.EMAIL_IN_REGISTER)
        Email_address.send_keys(email)
        password_element=self.browser.find_element(*LoginPageLocators.PASSWORD_IN_REGISTER)
        confirm_password_element=self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_IN_REGISTER)
        password_element.send_keys(password)
        confirm_password_element.send_keys(password)
        button=self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, "Login url is not corrected"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER_FORM), "Login gerister form is not presented"