import json

def loadDictionary(filename):
	dictionary = {}
	with open(filename) as fh:
	    for line in fh:
	        (key, val) = line.split()
	        dictionary[int(key)] = val
	return dictionary

#d = loadDictionary('register.txt')
#mail = d.get(1000)
#print(mail)

#print(json.dumps(d, indent=2, sort_keys=True))
