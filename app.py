from flask import Flask, render_template

app = Flask(__name__)

# корневой маршрут
@app.route('/')
def home():
    return render_template('cars.html')  # ваш HTML-файл в templates/cars.html

if __name__ == '__main__':
    # на Render debug=False
    app.run(host='0.0.0.0', port=5000)
