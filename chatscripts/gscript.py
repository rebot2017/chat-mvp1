import sys
if '/home/user/chat-mvp1/chatapp' not in sys.path:
	sys.path.append('/home/user/chat-mvp1/chatapp')
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
request_url = add_query_to_url("capital tower singapore")
api_response = retrieve_data_from_api(request_url)
print(api_response)
def get_json_from_str(json_string):
    return json.loads(json_string)
def gm_search(params):
    query = params.strip().replace(" ", "+")
    request_str = MAPS_BASIC_URL%(query,API_KEY)
    resp = requests.get(request_str)
    places = json.loads(resp.text)['results']
    print(places)
    
    result_objs = []
    for place in places:
        place_name = place['name']
        place_address = place['formatted_address']
        photo_request_url = ""
        if 'photos' in place:
            photo_request_url = MAPS_PHOTO_URL%(place['photos'][0]['photo_reference'], API_KEY)
        desc = "Address: " + place_address
        result_objs.append({'img': photo_request_url, 
                            'title': place_name, 
                            'description': desc,
                            ''
                           })
    return result_objs
import argparse

if __name__=="__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('search',help = '', type=str, nargs='+')
    args = argparser.parse_args()
    search = " ".join(args.search)
    search_res = gm_search(search)
    card1 = {"type":"string", data:"Search results from Google: "}
    card2 = {"type":"cards", data: []}
    card2.data = search_res
    return_arr = []
    return_arr.append(card1)
    return_arr.append(card2)
    return return_arr