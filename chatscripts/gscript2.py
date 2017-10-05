import argparse
import requests
import json
API_KEY = "AIzaSyAWd44FwD80rlxc8S6CZYUdjRQw_9cjeWg"
def gm_search(params):def gm_search(params):
    request_string = "https://maps.googleapis.com/maps/api/place/textsearch/json?query={0}&key={1}"
    query = params.strip().replace(" ", "+")
    req = request_string%(query, API_KEY)
    print(req)
    return req
#     print("request URL: %s"%(req))
#     resp = requests.get(req)
#     content = json.loads(resp.text)
#     return content
if __name__=="__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('search',help = '', type=str, nargs='+')
    args = argparser.parse_args()
    search = " ".join(args.search)
#     print("Fetching data for %s"%(search))
    
    data = gm_search(search)
#     print("Writing data to output file")
#     with open('gscript_results.json','w') as fp:
#         json.dump(data, fp)
        