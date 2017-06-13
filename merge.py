import json

with open('cities.json') as d:
	city = json.load(d)
with open('city_detailed.json') as d:
	city_d = json.load(d)
i=0
x=[]
for c in city:
	if c['name'].lower() in city_d.keys():
		x.append({})
		x[i]['name'] = c['name'].lower()
		x[i]['lat'] = city_d[c['name'].lower()]['latitude']
		x[i]['long'] = city_d[c['name'].lower()]['longitude']
		x[i]['state'] = c['state'].lower()
		i+=1
with open('city_merged.json','w') as d:
	 json.dump(x,d)
