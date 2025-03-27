from flask import Blueprint, request, jsonify
from services.weather_service import get_weather_report  # Ensure this is correct

# Define the Blueprint
weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/report', methods=['GET'])  # Route definition
def weather_report():
    city = request.args.get('city', 'London')  # Default to London if no city is provided
    weather_data = get_weather_report(city)
    return jsonify(weather_data)
