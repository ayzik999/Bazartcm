from flask import Flask, render_template

app = Flask(__name__)

@app.route('/cars')
def cars():
    return render_template('cars.html')

if __name__ == '__main__':
    app.run(debug=True)
