from selenium.webdriver.common.by import By
from behave import given, when, then
# from time import sleep

PROD_COUNT = (By.CSS_SELECTOR, 'div.product-count')
PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.product__title')


@given('open cure skin main page')
def open_main_page(context):
    context.app.main_page.open_main_page()


@given('open shop all')
def shop_all(context):
    context.app.product_page.shop_all()



