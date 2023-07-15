from selenium.webdriver.common.by import By
from pages.base_page import Page




class SearchPage(Page):
    SEARCH_BTN = (By.CSS_SELECTOR, 'div.search-modal.modal__content')
    SHOP_SELECT = (By.CSS_SELECTOR, "a[href='/collections/all']")

    def search_results(self):
        self.find_element(*self.SEARCH_BTN)

    def select_shops(self):
        self.find_element(*self.SHOP_SELECT)

