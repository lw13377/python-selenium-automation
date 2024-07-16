from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent']")


@given("Open target {item} page")
def item_page(context, item):
    context.driver.get(f'https://www.target.com/p/{item}')
    sleep(8)


@then('Verify that all colors work')
def click_and_verify_colors(context):
    expected_colors = ['Natural', 'Pink', 'Black']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'






















