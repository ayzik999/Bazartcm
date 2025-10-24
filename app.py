from flask import Flask, render_template, send_from_directory, jsonify
import json

app = Flask(__name__)

# Главная страница
@app.route("/")
def index():
    return render_template("index.html")

# Страница с автообъявлениями
@app.route("/cars")
def cars():
    return render_template("cars.html")

# Статика (если нужно явно)
@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory("static", path)

# JSON с объявлениями
@app.route("/ads.json")
def ads():
    with open("ads.json", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
