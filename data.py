import requests 
import json
import pickle

# Making a GET request 
# r = requests.get('https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22')
# data = json.loads(r.content)
# file = open("myfile.json", "w")
# json.dump(data, file, indent = 6)
# file.close()


def getData(l):
	return [{ date.split()[0] : {'Temperature' : j['temp'], 'Pressure' : j['pressure'], 'Wind' : w['speed'], 'Time' : date.split()[1] } } for j,w,date in [(i['main'],i['wind'],i['dt_txt']) for i in l]]

data = json.load(open('myfile.json'))

data = getData(data['list'])
# print(data)

d = dict()
for i in data:
	key = list(i.keys())[0]
	value = list(i.values())
	# print(key)
	# print(value)
	# print('*'*10)
	d[key] = d.get(key,[]) + value

# print(d)
file1 = 'data_dict'
outfile1 = open(file1,'wb')
pickle.dump(d,outfile1)
outfile1.close()