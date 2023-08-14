from selenium.webdriver.common.by import By
from pages.base_page import Page


class LandingPage(Page):

     UI_COMP = (By.CSS_SELECTOR, 'div.elementor elementor-30964')
     APP_DOWN = (By.CSS_SELECTOR, 'div.elementor-element.elementor-element-cbdfd7d.elementor-widget__width-auto.elementor-mobile-align…')
     PAGE_OPENS = (By.CSS_SELECTOR, 'span.VfPpkd-AznF2e-uDEFge.VfPpkd-AznF2e-uDEFge-OWXEXe-auswjd')

     def open_landing_page(self):
         self.open_url('https://cureskin.com/')


     def see_ui_comp(self):
         self.find_elements(*self.UI_COMP)


     def app_button(self):
         self.find_elements(*self.APP_DOWN)


     def verify_page_opens(self):
         self.open_url('https://app.curesk.in/KSjEbBWqQ')
         expected_page = self.find_elements(*self.PAGE_OPENS)
         print(expected_page)


         # assert expected_text == actual_text, \
             # f'Error! Expected {expected_text} bot got actual {actual_text}'



