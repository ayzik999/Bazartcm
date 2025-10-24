from flask import Flask, render_template, send_from_directory, jsonify
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cars")
def cars():
    return render_template("cars.html")

@app.route("/ads.json")
def ads():
    if os.path.exists("ads.json"):
        with open("ads.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []
    return jsonify(data)

@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory("static", path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
