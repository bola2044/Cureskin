from selenium.webdriver.common.by import By
from pages.base_page import Page


class ProductPage(Page):
    FIRST_RESULTS = (By.CSS_SELECTOR, 'div.card-wrapper')
    PROD_COUNT = (By.CSS_SELECTOR, 'div.product-count')
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.card-information__wrapper')
    PRODUCT_IMG = (By.CSS_SELECTOR, 'img.motion-reduce')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.price__sale')
    UI_COMP = (By.CSS_SELECTOR, 'div.elementor elementor-30964')

    def get_product_name(self):
        return self.find_element(*self. FIRST_RESULTS)

    def get_product_image(self):
        self.find_element(*self.PRODUCT_IMG)

    def get_product_price(self):
        return self.find_element(*self.PRODUCT_PRICE)


    def shop_all(self):
        self.open_url('https://shop.cureskin.com/collections/all')


    def verify_prod_count(self, expected_count):
        self.driver.find_element({expected_count}, *self.PROD_COUNT)
        self.verify_element_text('19 products', *self.PROD_COUNT)
        self.verify_element_text(expected_count, *self.PROD_COUNT)

