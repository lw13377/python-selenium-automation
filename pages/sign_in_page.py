from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    SIGN_IN_FROM_RIGHT = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    VERIFY_SIGN_IN_MSG = (By.XPATH, "//span[text()='Sign into your Target account']")

    def click_sign_in(self):
        self.click(*self.SIGN_IN)

    def click_sign_in_from_right(self):
        self.click(*self.SIGN_IN_FROM_RIGHT)

    def verify_sign_in_form(self):
        self.verify_text('Sign into your Target account', *self.VERIFY_SIGN_IN_MSG)