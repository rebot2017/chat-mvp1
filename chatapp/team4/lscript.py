import requests
import json
from bs4 import BeautifulSoup

query = "hotels in hong kong"

lazada_url = "http://www.lazada.sg/catalog/?&q=" + query.replace(" ", "%20")

search_result = requests.get(lazada_url)

soup = BeautifulSoup(search_result.text, 'html.parser')
result_divs = soup.find_all("div", class_= "c-product-card")
# print(result_divs)
result_obj = []
RESULT_LIMIT = 5
if len(result_divs) < 5:
    RESULT_LIMIT = len(result_divs)
for i in range(0, RESULT_LIMIT):
    imglink = result_divs[i].find('img')
    desc = result_divs[i].find("a", class_="c-product-card__name").text
    price = result_divs[i].find("span", class_="c-product-card__price-final").text
    result_obj = {'img': imglink,  'desc': desc, 'price':price}
    print(result_obj)