# Some of the libraries we need
import requests
from bs4 import BeautifulSoup
import json
def construct_url(ticker):
    base_url = "http://finance.yahoo.com/quote/{0}?p={0}"
    url = base_url.replace("{0}", ticker)
    return url
def retrieve_website(url):
    response = requests.get(url)
    html = response.text
    parsed_html = BeautifulSoup(html, 'html.parser')
    return parsed_html
def get_information(ticker, url, website):
    
    ticker_price = website.find("span", class_="Fz(36px)").getText()
    beta = website.find("td", {"data-test": "BETA-value"}).getText()
    
######## Add in your webscrapping code here to scrape more information #############
    
####################################################################################
######## Remember to add the information to the summary_data object below ##########

    summary_data = {
        'ticker': ticker,
        'ticker_price': ticker_price,
        'url': url
    }
    
    return summary_data
def get_ticker_data(ticker):
    
    url = construct_url(ticker)
    website = retrieve_website(url)

    summary_data = get_information(ticker, url, website)
    
    return summary_data


import argparse
import json

def parse_result(result):
    str = "Ticker: " + result['ticker'] + "\n"
    str += "Ticker Price: " + result['ticker_price'] + "\n"
    str += "more info: " + result['url'] + "\n"
    return str
    
def call_api(ticker):
    results = get_ticker_data(ticker)
    card1 = {"type": "string", "data": "getting results for %s"%ticker}
    card2 = {"type":"string", "data": parse_result(results)}
    return_arr = []
    return_arr.append(card1)
    return_arr.append(card2)
    return return_arr

if __name__=="__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('ticker',help = '')
    args = argparser.parse_args()
    ticker = args.ticker
    print(json.dumps(call_api(ticker)))