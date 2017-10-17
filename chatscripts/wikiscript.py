from bs4 import BeautifulSoup
import requests
import json
def wiki_search(query):
    query = query.strip().replace(" ", "%20")
    search_request_url = "https://en.wikipedia.org/w/api.php?action=query&list=search&srwhat=nearmatch&srsearch=%s&format=json&utf8="%(query)

    search_result = requests.get(search_request_url)
    json_result = json.loads(search_result.text)
    result_list = json_result['query']['search']
    if len(result_list) > 0:
        title = result_list[0]['title']
        article_request_url = "https://en.wikipedia.org/wiki/%s"%(title.replace(" ", "_"))
        result = requests.get(article_request_url)
        
        soup = BeautifulSoup(result.text, 'html.parser')
        first_paragraph = soup.find(attrs={'class': 'mw-parser-output'}).p.get_text()
        result_object = {'title': title, 'description': first_paragraph, "url": article_request_url}
        return result_object
    else:
        result_object = {'title': 'No match found on Wikipedia!', 'description': "", 'url':""}
        return result_object
import argparse

def parse_result(result):
    str = "Title: " + result['title'] + "\n"
    str+= "description: " + result['description'] + "\n"
    str+= "read more: " + result['url'] + "\n"
    return str

def call_api(title):
    result = wiki_search(title)
    card1 = {"type": "string", "data": "Searching wikipedia for %s"%title }
    card2 = {"type": "string", "data": parse_result(result)}
    return_arr = []
    return_arr.append(card1)
    return_arr.append(card2)
    return return_arr

if __name__=="__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('title',help = '', type=str, nargs='+')
    args = argparser.parse_args()
    title = " ".join(args.title)
    print(json.dumps(call_api(title)))



    