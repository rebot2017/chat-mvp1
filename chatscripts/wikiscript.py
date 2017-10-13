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
        result_object = {'title': title, 'description': first_paragraph, "URL": article_request_url}
        return result_object
    else:
        result_object = {'title': 'No match found on Wikipedia!', 'description': "", 'URL':""}
        return result_object
import argparse

if __name__=="__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('title',help = '', type=str, nargs='+')
    args = argparser.parse_args()
    title = " ".join(args.title)
    result = wiki_search(title)
    output = "Title: %s"%(result['title']) + "\n"
    if 'description' in result:
        output += "Article: %s"%(result['description'].encode("ASCII", "ignore")) + "\n"
    if 'URL' in result:    
        output += "Read more: %s"%(result['URL']) + "\n"
    print(output)

    