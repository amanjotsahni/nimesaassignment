import pickle

infile1 = open('data_dict','rb')
data = pickle.load(infile1)
infile1.close()

def fun(date, value):
	l = []
	for i in data.get(date, []):
		if(value == 1):
			l.append([i.get('Time', 'NO DATA AVAILABLE'),i.get('Temperature', 'NO DATA AVAILABLE')])
		elif value == 2:
			l.append([i.get('Time', 'NO DATA AVAILABLE'),i.get('Wind', 'NO DATA AVAILABLE')])
		elif value == 3:
			l.append([i.get('Time', 'NO DATA AVAILABLE'),i.get('Pressure', 'NO DATA AVAILABLE')])
	return l