
import httplib2
import json
api_key = "AIzaSyAWd44FwD80rlxc8S6CZYUdjRQw_9cjeWg"
def gmSearch(params):
    params = params.strip().replace(" ", "+")
    query = params
    req = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="+query+"&key="+api_key
    print(req)
    resp, content = httplib2.Http().request(req)
    contentjson = json.loads(content)
    msg = ""
    for res in contentjson["results"]:
        msg+="    Place Name: " + res["name"] + "\n"
        msg+="    Address: " + res["formatted_address"] + "\n"
        msg+="    place_id: " + res["place_id"] + "\n\n\n"
    return msg