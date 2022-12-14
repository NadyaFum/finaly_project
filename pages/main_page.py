import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage):
	def go_to_login_page(self):
		login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
		login_link.click()

	def should_be_login_link(self):
		assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"

	def test_guest_should_see_login_link(browser):
    		link = "http://selenium1py.pythonanywhere.com/"
    		page = MainPage(browser, link)
    		page.open()
    		page.should_be_login_link()