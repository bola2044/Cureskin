from selenium.webdriver.common.by import By
from pages.base_page import Page

class ProductPage(Page):
    FIRST_RESULTS = (By.CSS_SELECTOR, 'div.card-wrapper')
    PROD_COUNT = (By.CSS_SELECTOR, 'div.product-count')
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.product__title')

    def get_product_name(self):
        self.find_element(*self.FIRST_RESULTS)

    def shop_all(self):
        self.open_url('https://shop.cureskin.com/collections/all')

    def verify_prod_count(self, expected_count):
        self.driver.find_element({expected_count}, *self.PROD_COUNT)
        self.verify_element_text('19 products', *self.PROD_COUNT)
        self.verify_element_text(expected_count, *self.PROD_COUNT)
