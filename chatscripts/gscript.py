
import httplib2
import json
import argparse
api_key = "AIzaSyAWd44FwD80rlxc8S6CZYUdjRQw_9cjeWg"
def gm_search(params):
    params = params.strip().replace(" ", "+")
    query = params
    req = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="+query+"&key="+api_key
    resp, content = httplib2.Http().request(req)
    contentjson = json.loads(content.decode('utf8'))
    return content.decode('utf8')
if __name__=="__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('search',help = '', type=str, nargs='+')
    args = argparser.parse_args()
    search = " ".join(args.search)
    print("Fetching data for %s"%(search))
    json_data = gm_search(search)
    print("Writing data to output file")
    with open('gscript_results.json','w') as fp:
        json.dump(json_data,fp,indent = 4)
