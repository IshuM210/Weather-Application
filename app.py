from flask import Flask, render_template, request
import requests
import os

from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter

app = Flask(__name__)

# Enable Prometheus metrics
metrics = PrometheusMetrics(app)

# Counter WITH LABEL to track per-city search count
CITY_SEARCH_COUNT = Counter(
    'weather_city_search_total',
    'Number of times a city was searched',
    ['city']
)

API_KEY = "159f776152a2fd48e08898433586b7fe"  # Replace with your OpenWeather key

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    error = None

    if request.method == 'POST':
        city = request.form['city']
        
        # Increment Prometheus counter for THIS city
        CITY_SEARCH_COUNT.labels(city=city).inc()

        # API call (limit=1 improves local place match)
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&limit=1&appid={API_KEY}&units=metric"
        response = requests.get(url).json()
        print("API Response:", response)

        if response.get("cod") != 200:
            error = "City not found!"
        else:
            weather_data = {
                "city": response["name"],
                "temperature": response["main"]["temp"],
                "humidity": response["main"]["humidity"],
                "wind": response["wind"]["speed"],
                "description": response["weather"][0]["description"].title(),
                "icon": response["weather"][0]["icon"]
            }

    return render_template("home.html", weather=weather_data, error=error)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
