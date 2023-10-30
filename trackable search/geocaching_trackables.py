
import requests
from bs4 import BeautifulSoup
import re
from searchResults import extract_geocaching_codes
import time

#Checks geocache page for trackable code(s)
def checkGeocache(url):
    pattern = re.compile(r'^https://www\.geocaching\.com/track/')
    return pattern.match(url)

#Goes through geocaches and checks for trackables
codes = extract_geocaching_codes("Geocaching.com.html")
for code in codes:
    print (code)
    web_page_url = f'https://www.geocaching.com/geocache/{code}'
    try:
        response = requests.get(web_page_url)

        if response.status_code == 200:
            html_content = response.text

            soup = BeautifulSoup(html_content, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                href = link.get('href')
                if href and checkGeocache(href):
                    print(f"Found geocaching track URL: {href}")

        else:
            print(f"Failed to fetch the web page. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
input("No more codes")
