from bs4 import BeautifulSoup
import requests
def getContent(ticker):
    base_url = "http://finance.yahoo.com/quote/{0}?p={0}"
    url = base_url.replace("{0}", ticker)
    response = requests.get(url)
    html = response.text
    return html

def getHtml(html):
    return BeautifulSoup(html, 'html.parser')



