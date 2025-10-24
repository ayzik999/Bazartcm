from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Главная страница с категориями
@app.route('/')
def index():
    return render_template('index.html')

# Страница с объявлениями по категории
@app.route('/category/<cat>')
def category(cat):
    ads = []
    if os.path.exists('ads.json'):
        with open('ads.json', 'r', encoding='utf-8') as f:
            ads = json.load(f)
    # Фильтруем объявления по категории
    cat_ads = [ad for ad in ads if ad.get('category', 'Авто')==cat]
    return render_template('category.html', category=cat, ads=cat_ads)

# API для всех объявлений
@app.route('/ads.json')
def get_ads():
    if os.path.exists('ads.json'):
        with open('ads.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    return jsonify([])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
