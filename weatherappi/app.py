from flask import Flask
from controllers.weather_controller import weather_bp  # Ensure correct import

app = Flask(__name__)

# Register blueprint (Make sure this line exists)
app.register_blueprint(weather_bp, url_prefix='/api/weather')

# Debugging: Print all registered routes
print("Registered Routes:")
for rule in app.url_map.iter_rules():
    print(rule)

if __name__ == "__main__":
    app.run(debug=True)
