# This does not launch Chrome
# This will only navigate to https://www.google.com/search?q=instawork
# This will use beautifulsoup object to store and go through the page source to search for Instawork

import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from _ast import Assert

def search(search_key):

    #navigate to https://www.google.com/search?q=instawork
    url = 'https://www.google.com/search?q=' + search_key
    #print("url: " + url)
    source_code = requests.get(url)
    #plain_text = source_code.text

    # transaction to beautifulsoup object for easier sorting and searching
    soup = BeautifulSoup(source_code.content, 'html.parser')
    #soup = BeautifulSoup(plain_text)
    # GuessedAtParserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml").

    # this print out the whole content of the web page source
    #print(soup.prettify())

    # Tell Beautifulsoup to gather all the h3 with a class with the value 'BNeawe vvjwJb AP7Wnd'
    # looking for Instawork: Work Local Shifts 4+ - App Store
    link_position = 1
    title = ""

    for link in soup.findAll('div', {'class': 'BNeawe vvjwJb AP7Wnd'}):
        title = link.string
        print ("Title: " + title)

        if (title == "Instawork: Work Local Shifts 4+ - App Store"):
            # assert title == "Instawork: Work Local Shifts 4+ - App Store", "Unable to find Instawork: Work Local Shifts 4+ - App Store"
            assert title == "Instawork: Work Local Shifts 4+ - App Store", "This is not 'Instawork: Work Local Shifts 4+ - App Store'"
            print("Position: " + str(link_position) + " - Title: " + title)
            break
        else:
            link_position += 1




#Position: 1 - Title: Instawork
#Position: 2 - Title: Instawork Gigs & Jobs - Apps on Google Play
#Position: 3 - Title: Instawork: Work Local Shifts 4+ - App Store
#Position: 4 - Title: Instawork (@instaworkapp) • Instagram photos and videos
#Position: 5 - Title: Instawork: Flexible staffing solution for hourly workers and hospitality
#Position: 6 - Title: Instawork - LinkedIn
#Position: 7 - Title: 2 Instawork jobs in Canada - LinkedIn
#Position: 8 - Title: Instawork Reviews: What Is It Like to Work At Instawork? | Glassdoor


search('Instawork')
