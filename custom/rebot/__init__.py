from bs4 import BeautifulSoup
import requests
import json

headers = { "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36" }

def getContent(ticker):
    base_url = "https://finance.yahoo.com/quote/{0}?p={0}"
    url = base_url.replace("{0}", ticker)
    response = requests.get(url, headers = headers)
    content = response.text
    return content

def getHtml(content):
    return Readable(BeautifulSoup(content, 'html.parser'))


def getSoup(content):
    return BeautifulSoup(content, 'html.parser')


def createEmptyMessage():
    return Message()

class Readable: 
    soup = None
    def __init__(self, soup):
        self.soup = soup

    def search(self, tag, attribute = None, attributeValue = None):
        container = None
        if attribute is not None and attributeValue is not None:
            container = self.soup.find(tag, { attribute: attributeValue })
        else:
            container = self.soup.find(tag)
        
        if container is not None:
            return container.getText()
        else:
            return ""

    def __str__(self):
        return str(self.soup)

class Message: 
    context = []
    kvpairs = []

    def addData(self, key, value):
        self.kvpairs.append({key: value})

    def addText(self, text):
        self.context.append({"string": str(text)})

    def addLink(self, url, urlName = None):
        if urlName is not None:
            self.context.append({"link": json.dumps({url: urlName})})
        else: 
            self.context.append({"link": json.dumps({url: url})})

    def addImage(self, url):
        self.context.append({"image": url})

    def __str__(self):
        roots = []
        for item in self.context:
            for key, value in item.items():
                roots.append({"type": key, "data": value})

        kvdata = self.serializeKeyValues()
        if kvdata is not None:
            roots.append({"type": "kvpair", "data": kvdata})

        return json.dumps(roots)

    def serializeKeyValues(self):
        if len(self.kvpairs) == 0: return None
        keys = []
        values = []
        for item in self.kvpairs:
            for key, value in item.items():
                keys.append(key)
                values.append(value)
        return json.dumps([keys, values])
