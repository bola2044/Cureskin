from selenium.webdriver.common.by import By
from behave import given, when, then


PROD_COUNT = (By.CSS_SELECTOR, 'div.product-count')
PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.product__title')
UI_COMP = (By.CSS_SELECTOR, 'div.elementor elementor-30964')

@given('open cure skin main page')
def open_main_page(context):
    context.app.main_page.open_main_page()


@given('open shop all')
def shop_all(context):
    context.app.product_page.shop_all()





