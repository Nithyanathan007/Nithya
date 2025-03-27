from flask import Flask
from views import user_views

app = Flask(__name__)
app.register_blueprint(user_views)

if __name__ == "__main__":
    app.run(debug=True)