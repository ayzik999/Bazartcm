from flask import Flask, render_template, jsonify
import os, json

app = Flask(__name__)

# Главная страница с категориями
@app.route('/')
def index():
    categories = [
        {"name":"Авто","link":"cars"},
        {"name":"Недвижимость","link":"realestate"},
        {"name":"Работа","link":"jobs"},
        {"name":"Одежда, обувь, аксессуары","link":"clothes"},
        {"name":"Хобби и отдых","link":"hobby"},
        {"name":"Животные","link":"pets"},
        {"name":"Электроника","link":"electronics"}
    ]
    return render_template('index.html', categories=categories)

# Страница категории с объявлениями
@app.route('/<category>')
def category_page(category):
    ads_file = 'ads.json'
    if os.path.exists(ads_file):
        with open(ads_file, 'r', encoding='utf-8') as f:
            ads = json.load(f)
        # Фильтруем объявления по категории
        filtered = [ad for ad in ads if ad.get("category") == category]
    else:
        filtered = []
    return render_template('category.html', ads=filtered, category=category)

# API для загрузки всех объявлений
@app.route('/ads.json')
def get_ads():
    if os.path.exists('ads.json'):
        with open('ads.json', 'r', encoding='utf-8') as f:
            return jsonify(json.load(f))
    return jsonify([])

# Статика
@app.route('/static/<path:path>')
def send_static(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
