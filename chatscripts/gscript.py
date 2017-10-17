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
request_url = add_query_to_url("universal studios singapore")
api_response = retrieve_data_from_api(request_url)
print(api_response)
def get_json_from_str(json_string):
    return json.loads(json_string)
def extract_relevant_attributes(place_json):
    place_object = dict()
    place_object["title"] = place_json["name"]
    place_object["description"] = "address: " + place_json["formatted_address"]
    if 'photos' in place_json:
        place_object['img'] = MAPS_PHOTO_URL%(place_json['photos'][0]['photo_reference'], API_KEY)
    else:
        place_object['img'] = ""
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
def call_api(search):
    search_res = gm_search(search)
    card1 = {"type":"string", "data":"Search results from Google: "}
    card2 = {"type":"cards", "data": search_res}
    return_arr = []
    return_arr.append(card1)
    return_arr.append(card2)
    return return_arr
    
if __name__=="__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('search',help = '', type=str, nargs='+')
    args = argparser.parse_args()
    search = " ".join(args.search)
    print(json.dumps(call_api(search)))
    