# This will launch Chrome and search Instawork on google

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from _ast import Assert
import unittest


#driver = webdriver.Chrome('./chromedriver')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

# On google, search "Instawork"
search_bar = driver.find_element(by=By.NAME, value='q')
search_bar.clear()
search_bar.send_keys("Instawork")
search_bar.send_keys(Keys.RETURN)

#look for "Instawork" in search results
#search_result = driver.find_element(By.CLASS_NAME, value='BNeawe vvjwJb AP7Wnd')
# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":".BNeawe vvjwJb AP7Wnd"}

#search_result = driver.find_element_by_xpath("//h3[text()[contains(., 'Instawork')]]")
#AttributeError: 'WebDriver' object has no attribute 'find_element_by_xpath'

search_result = driver.find_element(By.XPATH, "//h3[contains(text(),'Instawork: Work Local Shifts 4+ - App Store')]")
# result: Instawork

result = search_result.text
print("result1: " + result)


# Confirm search result is indeed "Instawork". If not found, display error "Unable to find Instawork" and end the code
assert result == "Instawork: Work Local Shifts 4+ - App Store", "Unable to find Instawork"
print("You found me! - " + result)

driver.close()


