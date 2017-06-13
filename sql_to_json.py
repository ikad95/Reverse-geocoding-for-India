#!/home/moulik/anaconda2
#moulik adak
#12th june 2017

import pymysql,json

op={}
connection = pymysql.connect(host="localhost",
                     user="root",
                     password="hello",
                     db="loc")
try:
	with connection.cursor() as cursor:
		sql = "SELECT cellid,avg_lat,avg_long,locStr FROM ox_cellids where state is null;"
		cursor.execute(sql)
	connection.commit()
	results = cursor.fetchall()
	i = 0
	for result in results:
		op[result[3]] = (result[1],result[2])
		i+=1
	print str(i) + " results found"
finally:
	connection.close()

with open('cellid.json', 'w') as fp:
	json.dump(op, fp)
