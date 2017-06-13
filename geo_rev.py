#!/home/moulik/anaconda2
#moulik adak
#12th june 2017

import json,os,threading
from shapely.geometry import shape, Point
from concurrent.futures import ThreadPoolExecutor
from Queue import Queue

with open('india.geojson') as f:
    india = json.load(f)

with open('cellids.json') as c:
    locStrs = json.load(c)

states = {}

queue = Queue()

for feature in india['features']:
	states[feature["properties"]["NAME_1"]] = shape(feature['geometry'])
def get(locStr):
	point = Point(float(locStrs[locStr][1]),float(locStrs[locStr][0]) )
	for state in states:
		if states[state].contains(point):
				print locStr + " = " + state
				return ("update ox_locStrs set state='" + state + "', country='india' where state is null and locStrs=" + locStr + ";")

with ThreadPoolExecutor(max_workers=2) as executor:
	for ret in executor.map(get, locStrs):
		queue.put(ret)

file = open("update_query.txt","w")

while not queue.empty():
	try:
		file.write(queue.get()+"\n")
	except:
		pass
file.close()
