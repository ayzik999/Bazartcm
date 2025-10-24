from flask import Flask, render_template, request

app = Flask(__name__)

# Demo dataset
ADS = [
    {"id":1, "brand":"Toyota", "model":"Camry", "price":1250000, "currency":"сом", "color":"Белый", "condition":"used", "body":"Седан"},
    {"id":2, "brand":"Hyundai", "model":"Solaris", "price":690000, "currency":"сом", "color":"Серебристый", "condition":"used", "body":"Седан"},
    {"id":3, "brand":"Mercedes", "model":"C180", "price":4200000, "currency":"сом", "color":"Чёрный", "condition":"used", "body":"Седан"},
    {"id":4, "brand":"Kia", "model":"Rio", "price":730000, "currency":"сом", "color":"Красный", "condition":"used", "body":"Хэтчбек"},
    {"id":5, "brand":"BMW", "model":"Z4", "price":5800000, "currency":"сом", "color":"Синий", "condition":"new", "body":"Купе"}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cars")
def cars():
    # Фильтры через GET параметры
    brand = request.args.get("brand", "").lower()
    color = request.args.get("color", "").lower()
    condition = request.args.get("condition", "").lower()

    filtered_ads = ADS
    if brand:
        filtered_ads = [ad for ad in filtered_ads if ad["brand"].lower() == brand]
    if color:
        filtered_ads = [ad for ad in filtered_ads if ad["color"].lower() == color]
    if condition:
        filtered_ads = [ad for ad in filtered_ads if ad["condition"].lower() == condition]

    return render_template("cars.html", ads=filtered_ads)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
