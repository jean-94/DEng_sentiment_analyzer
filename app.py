from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/analyze/sentiment', methods=['GET', 'POST'])
def analyze_sentiment():
	speech = request.get_json()['speech']
	result = jsonify(speech)
	return result

if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0', port=4000)