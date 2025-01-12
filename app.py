from flask import Flask, jsonify, request
from scraper import get_weather, Cities

app = Flask(__name__)


@app.route('/')
def home():
    return """
    <h1>Welcome to the Weather Scraper API</h1>
    <p>Use the /weather endpoint to get weather information.</p>
    <p>Example usage: /weather?city=LosAngeles</p>
    """


@app.route('/weather', methods=['GET'])
def get_weather_data():
    city = request.args.get('city', 'LosAngeles')  # Default to Los Angeles if no city is provided
    city_code = getattr(Cities, city, None)
    if not city_code:
        return jsonify({"error": f"City '{city}' not found in the database."}), 404

    weather_data = get_weather(city_code)

    if isinstance(weather_data, dict):
        return jsonify(weather_data)
    else:
        return jsonify({"error": weather_data}), 500


if __name__ == '__main__':
    app.run(debug=True)
