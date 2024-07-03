from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep





@when('Click Sign in')
def sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    sleep(2)


@given('Click Sign in from right bar')
def right_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()


    sleep(4)


@then('Verify sign in form is there')
def verify_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")


    sleep(5)