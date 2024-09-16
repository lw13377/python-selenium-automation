from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    SIGN_IN_FROM_RIGHT = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    VERIFY_SIGN_IN_MSG = (By.XPATH, "//span[text()='Sign into your Target account']")
    EMAIL_LOGIN = (By.ID, "username")
    PASSWORD_LOGIN = (By.ID, "password")
    SIGN_WITH_PASS = (By.ID, "login")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='authAlertDisplay']")


    def click_sign_in(self):
        self.click(*self.SIGN_IN)

    def click_sign_in_from_right(self):
        self.click(*self.SIGN_IN_FROM_RIGHT)

    def verify_sign_in_form(self):
        self.verify_text('Sign into your Target account', *self.VERIFY_SIGN_IN_MSG)

    def type_email_or_phone(self):
        self.input_text('hasdasd@gmail.com', *self.EMAIL_LOGIN)

    def type_password(self):
        self.input_text('Beobeobe23!', *self.PASSWORD_LOGIN)

    def click_signin_with_pass(self):
        self.click(*self.SIGN_WITH_PASS)

    def verify_signin_error_msg(self):
        self.verify_text("We can't find your account.", *self.ERROR_MSG)
