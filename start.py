import requests
import json
import pandas as pd
from pandas.io.json import json_normalize   
import operator
import time

api_key=' PUT API KEY HERE'
headers = {'Authorization': 'Bearer %s' % api_key}
url = "https://api.yelp.com/v3/businesses/search"

dest_file = "output.json"

locations = ["Wien 1010", "Wien 1020", "Wien 1030", "Wien 1040",
             "Wien 1050", "Wien 1060", "Wien 1070", "Wien 1080",
             "Wien 1090", "Wien 1100", "Wien 1110", "Wien 1120",
             "Wien 1130", "Wien 1140", "Wien 1150", "Wien 1160",
             "Wien 1170", "Wien 1180", "Wien 1190", "Wien 1200",
             "Wien 1210", "Wien 1220", "Wien 1230"]

categories = ["Restaurants",
              "Cafes",
              "Bars",
              "Pubs",
              "Gastropubs",
              "Diners",
              "Nightlife",
              "Burgers",
              "Pizza",
              "Food",
              "Coffee & Tea"]

offsets = [0,50,100,150,200,250,300,350,400,450,500,
          550,600,650,700,750,800,850,900,950]


places = []


def get_biz(location,category,offset):
    loc = location
    cat = category
    off_s = offset
    params = {"location":"{}".format(loc), 
            "categories": "{}".format(cat),
            "limit":50,
             "offset":off_s}
    
    req = requests.get(url, params=params, headers=headers)
    parsed = json.loads(req.text)

    df = parsed["businesses"]
    for i in df:
        places.append(i)
    print("Fetched {} in {} with instance iterations of: {}".format(cat,loc,off_s))
    return None


for a in locations:
    for b in categories:
        for c in offsets:
            try:
                get_biz(a,b,c)
                for i in range(3,0,-1):
                    time.sleep(1)
                    print("{} seconds until next post".format(i))
            except:
                print("Encountered an error. Will reiterate.")
                




output_file = open(dest_file, 'w', encoding='utf-8')
for i in places:
    json.dump(i, output_file) 
    output_file.write("\n")