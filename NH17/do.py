from os import chdir
from pprint import pprint
chdir(r'c:\users\duco\documents\codejam\nh17')
f = open('in','r')
db={}
for n in range(1,284):
	db[n]={}
	db[n]["name"]=f.readline().split(' ')[1].strip()
	db[n]["country"]=f.readline().strip()
	db[n]["gender"]=f.readline().strip()
	assert db[n]["gender"] in ['F','M'], str(n)+' does not compute. \n'+str(db[n])
f.close()
origins = set(map(lambda x: db[x]['country'], db))
origin = "NETHERLANDS"
assert origin in origins, origin+' not found in '+origins
pprint( map(lambda y: db[y]['name'],
            filter(lambda x: db[x]['country']==origin, db))
        )
