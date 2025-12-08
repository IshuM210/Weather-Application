from flask import Flask, request, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import requests

app = Flask(__name__)

# ---------- PROMETHEUS COUNTER ----------
weather_counter = Counter(
    'weather_city_search_total',
    'Total number of weather city searches'
)

# ---------- WEATHER ROUTE ----------
@app.route('/weather')
def weather():
    city = request.args.get('city', 'chennai')

    # increase search count
    weather_counter.inc()

    # Dummy weather content (modify according to your app)
    return jsonify({
        "city": city,
        "temp": "30°C",
        "status": "sunny"
    })

# ---------- METRICS ROUTE ----------
@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

# ---------- HOME ----------
@app.route('/')
def home():
    return "Flask Prometheus Working!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
