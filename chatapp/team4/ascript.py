import requests
import json
from bs4 import BeautifulSoup

query = "home speaker"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}
amazon_url = "https://www.amazon.com/s/?url=field-keywords=" + query.replace(" ", "+")
print(amazon_url)
search_result = requests.get(amazon_url, headers = headers)
print(search_result.text)
soup = BeautifulSoup(search_result.text, 'html.parser')
# print(soup.prettify())
result_divs = soup.find_all("div", class_= "s-result-item celwidget")
print(result_divs)
result_obj = []
RESULT_LIMIT = 5
if len(result_divs) < 5:
    RESULT_LIMIT = len(result_divs)
for i in range(0, RESULT_LIMIT):
    imglink = result_divs[i].find('img').get('src')
    desc = result_divs[i].find("a", class_="s-access-detail-page  s-color-twister-title-link").get('title')
    price_span = result_divs[i].find("span", class_="sx-price")
    price = price_span.find("sx-price-whole").text + price_span.find("sx-price-fractional").text
    result_obj = {'img': imglink,  'desc': desc, 'price':price}
    print(result_obj)