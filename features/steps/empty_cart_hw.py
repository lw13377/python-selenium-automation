from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target')
def open(context):
    context.driver.get('https://www.target.com/')
    sleep(2)


@when('Click on Cart')
def click(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()

    sleep(2)


@then('Cart is Empty')
def cart(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    assert expected_text in actual_text, f"expected test {expected_text} does not match actual text {actual_text}"

    sleep(2)




