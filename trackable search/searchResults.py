from bs4 import BeautifulSoup

#Extract the geocaching codes from the geocaching search html page
def extract_geocaching_codes(html_file):
    geocachingCodes = []  
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')

    geocache_links = soup.find_all('a', href=lambda href: href and "/geocache/" in href)

    for link in geocache_links:
        href = link['href']
        geocaching_code = href.split('/geocache/')[1]
        geocachingCodes.append(geocaching_code)

    return geocachingCodes

