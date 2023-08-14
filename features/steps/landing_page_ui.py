from selenium.webdriver.common.by import By
from behave import given, when, then

UI_COMP = (By.CSS_SELECTOR, 'div.elementor elementor-30964')
APP_DOWN = (By.CSS_SELECTOR, 'div.elementor-element.elementor-element-cbdfd7d.elementor-widget__width-auto.elementor-mobile-align…')
ABOUT_US = (By.CSS_SELECTOR, 'a.elementor-item')
TESTM_PAGE = (By.CSS_SELECTOR, 'a.elementor-item')


@given('open cure skin page')
def open_landing_page(context):
    context.app.landing_page.open_landing_page()

@given('click on download app button')
def app_button(context):
    context.app.landing_page.app_button()


@then('user can click on about us')
def click_about_us(context):
    context.app.header_page.click_about_us()


@then('user can see ui components')
def see_ui_comp(context):
    context.app.landing_page.see_ui_comp()


@then('user can click on testimonials')
def testimonials_button(context):
    context.app.header_page.testimonials_button()


@then('verify correct page opens')
def verify_page_opens(context):
    context.app.landing_page.verify_page_opens()

@then('verify about us page opens {expected_page}')
def about_us_page_opens(context, expected_page):
    context.app.header_page.about_us_page_opens()

@then('verify correct page opens {expected}')
def verify_testimonials_page(context, expected):
    context.app.header_page.verify_testimonials_page()