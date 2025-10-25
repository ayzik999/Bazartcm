from flask import Flask, render_template, jsonify
import json, os

app = Flask(__name__)

# ====== ROUTES ======
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/category')
def category():
    return render_template('category.html')

@app.route('/cars')
def cars():
    # Загружаем список объявлений
    with open('ads.json', 'r', encoding='utf-8') as f:
        ads = json.load(f)
    return render_template('cars.html', ads=ads)

@app.route('/api/ads')
def api_ads():
    with open('ads.json', 'r', encoding='utf-8') as f:
        ads = json.load(f)
    return jsonify(ads)

# ====== MAIN ======
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
