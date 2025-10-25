from flask import Flask, render_template, jsonify
import json, os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cars')
def cars():
    return render_template('cars.html')

@app.route('/category')
def category():
    return render_template('category.html')

@app.route('/api/ads')
def api_ads():
    with open('ads.json', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
