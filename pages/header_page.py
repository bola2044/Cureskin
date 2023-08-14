from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class HeaderPage(Page):
  ABOUT_US = (By.CSS_SELECTOR, 'a.elementor-item')
  TESTM_PAGE = (By.CSS_SELECTOR, 'a.elementor-item')

  def click_about_us(self):
      self.find_element(*self.ABOUT_US).click()
      sleep(10)

  def about_us_page_opens(self):
      self.open_url('https://cureskin.com/about-cureskin/')
      expected_page = self.find_element(*self.ABOUT_US).text
      print(expected_page)

      sleep(6)

  def testimonials_button(self):
      self.find_element(*self.TESTM_PAGE).click()
      sleep (5)


  def verify_testimonials_page(self):
      self.open_url('https://cureskin.com/testimonials/')
      expected = self.find_element(*self.TESTM_PAGE).text
      print(expected)
