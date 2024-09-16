from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import then, when, given
from time import sleep


@when('Enters wrong email')
def wrong_email(context):
    context.app.sign_in_page.type_email_or_phone()


@when('Enters wrong password')
def wrong_password(context):
    context.app.sign_in_page.type_password()


@when('Enter sign in')
def sign_in(context):
    context.app.sign_in_page.click_signin_with_pass()


@then('Verifies that error message is shown')
def verify_error_for_sign_in(context):
    context.app.sign_in_page.verify_signin_error_msg()