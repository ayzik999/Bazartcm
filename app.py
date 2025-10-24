from flask import Flask, render_template, jsonify
import json, os

app = Flask(__name__)

# Главная
@app.route('/')
def index():
    return render_template('index.html')

# Страница категории
@app.route('/category/<name>')
def category_page(name):
    ads = []
    if os.path.exists('ads.json'):
        with open('ads.json','r',encoding='utf-8') as f:
            data = json.load(f)
        ads = [ad for ad in data if ad['title'].lower().find(name.lower())!=-1]
    return render_template('category.html', category=name, ads=ads)

if __name__ == '__main__':
    app.run(debug=True)
