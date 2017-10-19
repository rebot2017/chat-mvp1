import argparse
import requests
import json
API_KEY = "AIzaSyAWd44FwD80rlxc8S6CZYUdjRQw_9cjeWg"
MAPS_SEARCH_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=%s&key=%s"
MAPS_PHOTO_URL = "https://maps.googleapis.com/maps/api/place/photo?photoreference=%s&maxheight=400&key=%s"
def add_query_to_url(search_query):
    query = search_query.strip().replace(" ", "+") #replace the spaces in the query with +
    search_request_url = MAPS_SEARCH_URL%(query, API_KEY) #add the search query to the URL
    return search_request_url
def retrieve_data_from_api(url):
    response = requests.get(url) #calling the API endpoint
    return response.text #extracting the results from the response object
def get_json_from_str(json_string):
    return json.loads(json_string)
def extract_relevant_attributes(place_json):
    place_object = dict()
    place_object["title"] = place_json["name"]
    if 'photos' in place_json:
        place_object['img'] = MAPS_PHOTO_URL%(place_json['photos'][0]['photo_reference'], API_KEY)
    else:
        place_object['img'] = ""
        
    ## place_object is a container for what we want to provide to the chatbot.
    ## Looking at the json google returned, what other attributes do you think are relevant? 
    ## Put what you think are relevant in a string, and set it as `description` attribute of the place_object
    ## i.e. place_object['description'] = ....
    ##############################################################
    ################### Your code here ###########################
    
    
    
    ##############################################################
    return place_object
def get_places(places_json):
    places_object = []
    for place in places_json:
        places_object.append(extract_relevant_attributes(place))
    return places_object
def gm_search(search_query):
    url = add_query_to_url(search_query)
    
    response = retrieve_data_from_api(url)
    
    response_json = get_json_from_str(response)
    
    places = get_places(response_json['results'])
    
    return places

    
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