import requests
import json
from bs4 import BeautifulSoup
def bookdepo_search(query):
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
    }
    bookdepo_url = "https://www.bookdepository.com/search?search=Find+book&searchTerm=" + query.replace(" ", "+")
    search_result = requests.get(bookdepo_url, headers = headers)
    soup = BeautifulSoup(search_result.text, 'html.parser')
    result_divs = soup.find_all("div", class_= "book-item")

    result_obj = []
    RESULT_LIMIT = 5
    if len(result_divs) < RESULT_LIMIT:
        RESULT_LIMIT = len(result_divs)
    for i in range(0, RESULT_LIMIT):
        imglink = result_divs[i].find('img').get('data-lazy')
        book_title = result_divs[i].find("h3", class_="title").getText().strip()
        book_author = result_divs[i].find("p", class_="author").getText().strip()
        book_published_date = result_divs[i].find("p", class_="published").getText().strip()
        book_format = result_divs[i].find("p", class_="format").getText().strip()
        
        desc = book_title +"\n Author: " + book_author + "\nPublished: " + book_published_date + "\nFormat: " + book_format
        price = result_divs[i].find("p", class_="price").text.strip()
        result_obj.append({'img': imglink,  'description': desc, 'price':price})
    return result_obj
import argparse

if __name__=="__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('title',help = '', type=str, nargs='+')
    args = argparser.parse_args()
    title = " ".join(args.title)
    print(json.dumps(bookdepo_search(title)))
