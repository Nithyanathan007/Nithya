class Weather:
    def __init__(self, city, temperature, description, humidity, wind_speed):
        self.city = city
        self.temperature = temperature
        self.description = description
        self.humidity = humidity
        self.wind_speed = wind_speed

    def to_dict(self):
        return {
            "city": self.city,
            "temperature": self.temperature,
            "description": self.description,
            "humidity": self.humidity,
            "wind_speed": self.wind_speed
        }
