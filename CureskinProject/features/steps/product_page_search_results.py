from selenium.webdriver.common.by import By
from behave import given, when, then

PROD_COUNT = (By.CSS_SELECTOR, 'div.product-count')
PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.product__title')
PRODUCT_IMG = (By.ID, 'span#ProductImages')
PRODUCT_PRICE = (By.ID, 'div#price-template--17185951023421__main.no-js-hidden')


@then('verify user can see {expected_count} products for cure')
def verify_prod_count(context,expected_count):
    actual_text = context.driver.find_element(*PROD_COUNT)
    assert expected_count == actual_text, f'Expected {expected_count}, but got {actual_text}'
    context.app.product_page.verify_prod_count(actual_text)


@then('Verify first results have name,image and price')
def get_product_name(context):
    context.app.product_page.get_product_name()