from flask import Flask, request, jsonify

api = Flask(__name__)

uname = "admin"
pswd = "123"

@api.route('/', methods=['GET','POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid request"}), 400
    
    username = data.get("username")
    password = data.get("password")

    if username == uname and password == pswd:
        return jsonify({"message": "Login success"}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

if __name__ == '__main__':
    api.run(debug=True)
