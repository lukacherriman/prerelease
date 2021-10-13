import xml.etree.ElementTree as Et
import urllib.request

def loadRSS():
    rssurl ='http://feeds.bbci.co.uk/news/rss.xml?edition=uk'
    response = urllib.request.urlopen(rssurl)
    return response.read()


def parseXML(data):
    root = Et.fromstring(data)
    news_items = []
    for item in root.findall('./channel/item'):
        for child in item:
            "print(child.tag, child.text)"
            news_items.append(child)
    return(news_items)

data = loadRSS()
root = Et.fromstring(data)

news_items = parseXML(data)
articles = 5

for i in range(2, 5*articles, 5):
    print(news_items[i-2].tag, news_items[i-2].text)
    print(news_items[i].tag, news_items[i].text)
