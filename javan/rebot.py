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

def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None

class Readable: 
    def __init__(self, soup = None):
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
    def __init__(self):
        self.__context = []
        self.__kvpairs = []

    @property
    def data(self):
        return json.dumps(self.__kvpairs, sort_keys=False, indent=2)
    
    @property
    def info(self):
        return json.dumps(self.__context, sort_keys=False, indent=2)

    def addData(self, key, value):
        self.__kvpairs.append({key: value})

    def addText(self, text):
        self.__context.append({"string": str(text)})

    def addLink(self, url, urlName = None):
        if urlName is not None:
            self.__context.append({"link": json.dumps([url, urlName])})
        else: 
            self.__context.append({"link": json.dumps([url, url])})

    def addImage(self, url):
        self.__context.append({"image": url})

    def __build(self):
        roots = []
        for item in self.__context:
            for key, value in item.items():
                roots.append({"type": key, "data": value})

        kvdata = self.serializeKeyValues()
        if kvdata is not None:
            roots.append({"type": "kvpair", "data": kvdata})
        return roots

    def __str__(self):
        return json.dumps(self.__build(), sort_keys=False, indent=2)

    # make callable
    def __call__(self):
        print(json.dumps(self.__build()))

    def serializeKeyValues(self):
        if len(self.__kvpairs) == 0: return None
        keys = []
        values = []
        for item in self.__kvpairs:
            for key, value in item.items():
                keys.append(key)
                values.append(value)
        return json.dumps([keys, values])
        