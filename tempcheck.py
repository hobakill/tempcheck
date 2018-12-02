#!/usr/bin/env python3

import geocoder
import argparse
import json
import os
from darksky import forecast
tomkey = os.environ['tomkey']
darkkey = os.environ['darkkey']

locations = {
        'work': '1060 W Addison St, Chicago',
        'home': '1060 W Addison St, Chicago, IL 60613 ',
        'cabin': '1060 W Addison St. 60613'
        }

parser = argparse.ArgumentParser(description='Weather, son.')
parser.add_argument('locations', nargs='?', const=1, default="home", help='name of city, state')
args = parser.parse_args()

def wx(location):
    latlng =  geocoder.tomtom(location, key=tomkey).latlng
    info = forecast(darkkey, latlng[0], latlng[1])
    wx = json.dumps({
        "current_temp": info.temperature,
        "current_dew_point": info.dewPoint,
        "todays_high": info['daily']['data'][0]['temperatureHigh'],
        "summary": info['hourly']['summary']})
    return wx

print(wx(locations.get(args.locations, args.locations)))
