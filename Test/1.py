from flask import Flask, request, render_template, url_for
api = Flask(__name__)
uname = "admin"
pswd = "123"
@api.route('/', methods=['GET','POST'])
def login():
    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']

        if username == uname and password == pswd:
         return "login success"
        else:
           return" Invalid username or password.Try again."
    return  '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''
if __name__ =='__main__':
  api.run(debug=True)