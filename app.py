from flask import Flask, render_template, jsonify, send_from_directory
import os
import json

app = Flask(__name__)

ADS_FILE = "ads.json"

# Главная страница
@app.route("/")
def index():
    return render_template("index.html")

# Страница автообъявлений
@app.route("/cars")
def cars():
    return render_template("cars.html")

# API для объявлений
@app.route("/ads.json")
def ads():
    if os.path.exists(ADS_FILE):
        with open(ADS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data)
    return jsonify([])

# Статика (изображения/стили)
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
