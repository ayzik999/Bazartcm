from flask import Flask, render_template, jsonify, abort
import json, os

app = Flask(__name__)

def load_ads():
    with open('ads.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# корень
@app.route('/')
def index():
    return render_template('index.html')

# категория (пример)
@app.route('/category')
def category():
    return render_template('category.html')

# страница со всеми автомобилями (по-прежнему)
@app.route('/cars')
def cars():
    ads = load_ads()
    return render_template('cars.html', ads=ads)

# API для фронта
@app.route('/api/ads')
def api_ads():
    return jsonify(load_ads())

# детальная страница объявления
@app.route('/car/<int:ad_id>')
def car_detail(ad_id):
    ads = load_ads()
    for ad in ads:
        if int(ad.get('id', -1)) == ad_id:
            return render_template('car.html', ad=ad)
    # если не найдено
    abort(404)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # debug=False для продакшена, но локально можно включать
    app.run(host='0.0.0.0', port=port, debug=True)
