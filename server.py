from flask import Flask, request, render_template
import json
from deploycode import fun

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


app = Flask(_name_)
@app.route("/")
def index():
	return render_template('index.html')


@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return """Server shutting down...\n Thank you for visiting!"""

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


if _name_ == "_main_":
	app.run(debug = True, port = 9999)
