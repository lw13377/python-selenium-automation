from behave import given, when, then
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep



@given('Open Target')
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(2)


@when('search for {product}')
def search_for_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    sleep(2)


@then('find results')
def find_results(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    sleep(4)


@then('clear search')
def find_results(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/ResetButton']").click()
    sleep(2)


@then('add tea to the cart')
def add_tea_to_cart(context):
    context.driver.execute_script("window.scrollBy(0, 670)")
    context.driver.find_element(By.ID, "addToCartButtonOrTextIdFor12953662").click()
    sleep(2)


@then('add coffee to the cart')
def add_coffee_to_cart(context):
    context.driver.execute_script("window.scrollBy(0, 670)")
    context.driver.find_element(By.ID, "addToCartButtonOrTextIdFor14072552").click()
    sleep(3)


@then('confirm add item to cart')
def confirm_add_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='orderPickupButton']").click()
    sleep(3)


@then('continue shopping')
def continue_shopping(context):
    context.driver.find_element(By.XPATH, "//button[text()='Continue shopping']").click()
    sleep(3)


@then('checkout cart')
def check_out_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/cart']").click()
    sleep(1)

@then('verify cart items')
def verify_cart_items(context):
    context.driver.find_element(By.XPATH, "//span[text()='2 items']")





@given('Open Circle Target Page')
def open_circle_target(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')


@then('Verify 10 Links')
def verify_links(context):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='@web/slingshot-components/CellsComponent/Link']")
    assert len(links) == 10, f"expected 10 links, got {len(links)}"



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

    sleep(3)


@when('Click on Cart')
def click_on_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()

    sleep(2)


@then('Cart is Empty')
def cart(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    assert expected_text in actual_text, f"expected test {expected_text} does not match actual text {actual_text}"

    sleep(2)




