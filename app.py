from flask import Flask, render_template, request, jsonify
from SentimentAnalyser import SentimentAnalyserText

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/analyze/sentiment', methods=['GET', 'POST'])
def analyze_sentiment():
	speech = request.get_json()['speech']
	return jsonify(SentimentAnalyserText(speech))
	
if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0', port=4000)