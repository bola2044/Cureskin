from selenium.webdriver.common.by import By
from behave import given, when, then



FIRST_RESULTS = (By.CSS_SELECTOR, 'div.card-wrapper')
PROD_COUNT = (By.CSS_SELECTOR, 'div.product-count')
PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.card-information__wrapper')
PRODUCT_IMG = (By.CSS_SELECTOR, 'img.motion-reduce')
PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.price__sale')


@then('verify user can see {expected_count} products for cure')
def verify_prod_count(context,expected_count):
    actual_text = context.driver.find_element(*PROD_COUNT)
    assert expected_count == actual_text, f'Expected {expected_count}, but got {actual_text}'
    context.app.product_page.verify_prod_count(actual_text)


@then('Verify first results have name')
def get_product_name(context):
    context.app.product_page.get_product_name()


@then('Verify first results have an image')
def get_product_image(context):
    context.app.product_page.get_product_image()
    all_products = context.driver.find_elements(*FIRST_RESULTS)
    print(all_products)


    @then('Verify first results have a price')
    def get_product_price(context):
        context.app.product_page.get_product_price()
        product_price = context.driver.find_elements(*PRODUCT_PRICE)
        print(product_price)

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE)
        print(title)
        assert title, 'Title should not be blank'
        # assert product.find_element(*PRODUCT_IMG).is_displayed(), 'Image is not found'
        assert product.find_element(*PRODUCT_PRICE).is_displayed(), 'Price is not found'






