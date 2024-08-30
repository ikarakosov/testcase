from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from time import sleep


app = Flask(__name__)
metrics = PrometheusMetrics(app)


# Главный эндпоинт, который возвращает статус 200 и информацию о сервере
@app.route('/')
def home():
    return jsonify({
        "message": "Hello, this is your Flask web server!",
        "status": "running"
    }), 200

# Эндпоинт для проверки статуса сервера
@app.route('/status')
def status():
    return jsonify({
        "status": "OK",
        "code": 200
    }), 200

@app.route('/wait')
def wait():
    sleep(0.5)
    return jsonify({
        "sleep": "Well",
        "code": 200
    }), 200

@app.route('/longwait')
def longwait():
    sleep(10)
    return jsonify({
        "sleep": "Awesome",
        "code": 200
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
