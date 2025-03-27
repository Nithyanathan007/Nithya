rom flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Dummy user data (replace with a database in real-world scenarios)
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            session['user'] = username  # Store username in session
            return redirect(url_for('dashboard'))
        else:
            return "Invalid username or password. Try again."
    
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''
    

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return f'Welcome, {session["user"]}! <a href="/logout">Logout</a>'
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
