import json,os,threading
from shapely.geometry import shape, Point
from concurrent.futures import ThreadPoolExecutor
from Queue import Queue


with open('cellids.json') as c:
    locStrs = json.load(c)
file = open('res_dist.txt','w')
with open('india_detailed.geojson') as f:
    india = json.load(f)
dists={}
for feature in india['features']:
	dists[feature["name"]] = shape(feature['geometry'])

def get(locStr):
	lng = locStrs[locStr][1]
	lat = locStrs[locStr][0]
	point = Point(float(lng),float(lat) )
	for dist in dists:
		if dists[dist].contains(point):
				print("latitude="+str(lat)+"&longitude="+str(lng)+ " = " +str(dist))
				return 1
	return 0

#				return ("update ox_locStrs set state='" + str(dist) + "', country='india' where state is null and locStrs=" + locStr + ";")
fail,succ=0,0
for i in locStrs:
	x=get(i)
	if(x==0):
		fail+=1
	else:
		succ+=1
print succ,fail,succ/float(fail+succ)*100
