import argparse
import requests
import json
API_KEY = "AIzaSyAWd44FwD80rlxc8S6CZYUdjRQw_9cjeWg"
MAPS_BASIC_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=%s&key=%s"
MAPS_PHOTO_URL = "https://maps.googleapis.com/maps/api/place/photo?photoreference=%s&maxheight=400&key=%s"
def gm_search(params):
    query = params.strip().replace(" ", "+")
    request_str = MAPS_BASIC_URL%(query,API_KEY)
    resp = requests.get(request_str)
    places = json.loads(resp.text)['results']
    
    result_objs = []
    for place in places:
        place_name = place['name']
        place_address = place['formatted_address']
        photo_request_url = ""
        if 'photos' in place:
            photo_request_url = MAPS_PHOTO_URL%(place['photos'][0]['photo_reference'], API_KEY)
        desc = "Address: " + place_address
        result_objs.append({'img': photo_request_url, 'title': place_name, 'description': desc})
    return result_objs
import argparse

if __name__=="__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('search',help = '', type=str, nargs='+')
    args = argparser.parse_args()
    search = " ".join(args.search)
    print(json.dumps(gm_search(search), indent=4))
