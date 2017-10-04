
import argparse
import requests
import json
api_key = "AIzaSyAWd44FwD80rlxc8S6CZYUdjRQw_9cjeWg"
def gm_search(params):
    params = params.strip().replace(" ", "+")
    query = params
    req = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="+query+"&key="+api_key
    print("request URL: %s"%(req))
    resp = requests.get(req)
    content = json.loads(resp.text)
    return content
if __name__=="__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('search',help = '', type=str, nargs='+')
    args = argparser.parse_args()
    search = " ".join(args.search)
    print("Fetching data for %s"%(search))
    data = gm_search(search)
    print("Writing data to output fe")
    with open('gscript_results.json','w') as fp:
        json.dump(data, fp)
        