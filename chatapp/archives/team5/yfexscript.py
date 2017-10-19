import requests
from bs4 import BeautifulSoup
import json
import argparse

EXCHANGE_RATE_YAHOO_URL = 'https://finance.yahoo.com/quote/%s=X'

def exchange_rate_search(params):
    query = params.replace(" ","").upper()

    request_url = EXCHANGE_RATE_YAHOO_URL%(query)
    print(request_url)
    resp = requests.get(request_url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    # print(soup.prettify())
    day_range = soup.find("td", {"data-test": "DAYS_RANGE-value"})
    if day_range is not None:
        return day_range.getText()


if __name__=="__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('currencies',help = '', type=str, nargs='+')
    args = argparser.parse_args()
    currencies = " ".join(args.currencies)
    print(exchange_rate_search(currencies))