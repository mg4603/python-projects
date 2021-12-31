import requests
import xml.etree.ElementTree as ET

RSS_FEED_URL = 'https://news.google.com/news?q=apple&output=rss'

def load(url):
    resp = requests.get(url)
    return resp.content

def parseXML(rss):
    root = ET.fromstring(rss)
    newsitems = []

    for item in root.findall('./channel/item'):
        news = {}
        
        for child in item:
            news[child.tag] = child.text.encode('utf-8')

        newsitems.append(news)
    return newsitems

def topstories():
    rss = load(RSS_FEED_URL)

    return parseXML(rss)

