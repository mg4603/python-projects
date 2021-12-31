import requests
import xml.etree.ElementTree as ET

RSS_FEED_URL = "https://cointelegraph.com/rss"

def loadRSS(url):
    try:
        response = requests.get(url)
        return response.content
    except Exception as e:
        print(e)
        return None

def parseXML(rss):
        
    root = ET.fromstring(rss)

    news_items = []

    for item in root.findall('./channel/item'):
        news = {}
        if 'shib' not in item.find('title'):
            continue

        for child in item:
                if child.tag == '{http://search.yahoo.com/mrss/}content':
                    news['media'] = child.attrib['url']
                else:
                    news[child.tag] = child.text.encode('utf-8')
        news_items.append(news)
    return news_items

def shib_news():
    return parseXML(loadRSS(RSS_FEED_URL))

shib_news()
