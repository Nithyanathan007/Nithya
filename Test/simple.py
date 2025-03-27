from flask import Flask, request
api = Flask(__name__)
@api.route('/', methods=['GET'])
def login():
    return "LOGIN"
@api.route('/post', methods=['POST'])
def usp():
   if request.method=="post":
      username = request.form["username"]
      password = request.form["password"]
   elif username == 'welcome' and password == '123':
       return "sussesfully login"
 
if __name__ =='__main__':
  api.run(debug=True)
