from behave import step
from selenium.webdriver.common.keys import Keys

import requests
from bs4 import BeautifulSoup

from pageobjects.google_page import HomePage
from pageobjects.search_result_page import SearchResultPage


@step('I go to Google')
def i_go_to_google(context):
    context.driver.get(context.app_url)


@step('I search for "Instawork"')
def i_search_for_instawork(context):
    page = HomePage(context)
    page.search_bar.clear()
    page.search_bar.send_keys("Instawork")
    page.search_bar.send_keys(Keys.RETURN)


# Used for Scenario: Search Instawork on Google
@step('I should see "Instawork: Work Local Shifts 4+ - App Store"')
def i_should_see_instawork_work_local_shifts_4_app_store(context):
    page = SearchResultPage(context)
    result = page.search_result.text
    print("result1: " + result)
    # Confirm search result is indeed "Instawork". If not found, display error "Unable to find Instawork" and end the code
    assert result == "Instawork: Work Local Shifts 4+ - App Store", "Unable to find Instawork"
    print("You found me! - " + result)


# Used for Scenario: Search Instawork on Google and find its position
@step('I should see "Instawork: Work Local Shifts 4+ - App Store" and its position')
def i_should_see_instawork_work_local_shifts_4_app_store_and_its_position(context):
    url = context.driver.current_url
    print("URL: " + url)
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.content, 'html.parser')

    link_position = 1
    title = ""

    for link in soup.findAll('div', {'class': 'BNeawe vvjwJb AP7Wnd'}):
        title = link.string
        print("Title: " + title)

        if (title == "Instawork: Work Local Shifts 4+ - App Store"):
            assert title == "Instawork: Work Local Shifts 4+ - App Store", \
                "This is not 'Instawork: Work Local Shifts 4+ - App Store'"

            print("Position: " + str(link_position) + " - Title: " + title)
            break
        else:
            link_position += 1
