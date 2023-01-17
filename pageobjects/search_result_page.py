''''
This page search for "Instawork: Work Local Shifts 4+ - App Store" on Search result page
'''

from pageobjects.base_page import BasePage
from selenium.webdriver.common.by import By
from splinter import browser
import requests


class SearchResultPage(BasePage):
    search_result_loc = (By.XPATH, "//h3[contains(text(),'Instawork: Work Local Shifts 4+ - App Store')]")

    @property
    def search_result(self):
        return self.driver.find_element(*self.search_result_loc)