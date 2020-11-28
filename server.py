import pickle
from flask import Flask, request, jsonify, render_template
import json
from deploycode import fun

app = Flask(__name__)
@app.route("/")
def index():
	return render_template('index.html')

@app.route("/result", methods = ['GET'])
def calc_xor_Predict():
	value = int(request.args['w'])
	date = request.args['date']
	
	print()
	print(value,date)
	print('*'*10)
	res =  fun(date,value)
	res = json.dumps(res)
	di = {1: 'Weather', 2: 'Wind Speed', 3: 'Pressure'}
	return render_template('result.html', res = res, d = date, v = di.get(value))
	#return json.dumps(res)


if __name__ == "__main__":
	app.run(debug = True, port = 8791)