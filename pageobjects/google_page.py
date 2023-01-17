''''
This page goes to Google
And search Instawork
'''

from pageobjects.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    search_bar_loc = (By.NAME, 'q')

    @property
    def search_bar(self):
        return self.driver.find_element(*self.search_bar_loc)

