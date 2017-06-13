#!/usr/bin/env python

#moulik adak
#12th june 2017

import json,os,threading
from shapely.geometry import shape, Point
from concurrent.futures import ThreadPoolExecutor
from Queue import Queue

with open('india.geojson') as ff:
	india = json.load(ff)

with open('test.json') as c:
	cellids = json.load(c)

states = {}

queue = Queue()
global succ
global fail
fail = 0
succ = 0
EPS = 1.2e-16
for feature in india['features']:
	states[feature["properties"]["NAME_1"]] = shape(feature['geometry'])
def get(cellid):
	point = Point(float(cellid['lon']),float(cellid['lat']) )
	for state in states:
		if states[state].contains(point) and state == cellid['state'].lower():
			print state,cellid['state'],cellid['name'],"Success"
			return 1
		if states[state].contains(point) and state != cellid['state'].lower():
			print state,cellid['state'],cellid['name'],"Fail"
			return -1
	return 0

for obj in cellids:
	if get(obj) > 0:
		succ+=1
	else:
		fail+=1

print succ,fail,succ/float(succ+fail) *100,"%"
