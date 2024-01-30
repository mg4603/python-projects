from requests import get
from bs4 import BeautifulSoup
from random import shuffle

TITLE_COUNT = 0

def scrape(url):
    global TITLE_COUNT

    response = get(url = url)

    soup = BeautifulSoup(response.content, 'html.parser')
    
    title = soup.find(id="firstHeading")
    print(title.text)
    
    all_links = soup.find(id='bodyContent').find_all('a')
    shuffle(all_links)
    
    for link in all_links:
        if link['href'].find('/wiki/') == -1:
            continue

        linkToScrape = link['href']
        break


    TITLE_COUNT += 1
    if TITLE_COUNT == 10:
        return

    scrape('https://en.wikipedia.org' + linkToScrape)
    

scrape("https://en.wikipedia.org/wiki/Web_scraping")
