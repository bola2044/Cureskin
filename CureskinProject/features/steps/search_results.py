from selenium.webdriver.common.by import By
from behave import given, when, then


SEARCH_BTN = (By.ID, 'input#Search-In-Modal')
SHOP_SELECT = (By.CSS_SELECTOR, "a[href='/collections/all']")


@when('user click search button')
def search_results(context):
    context.app.search_page.search_results()


@then('Select shop all to open page')
def select_shops(context):
    context.app.search_page.select_shops()
