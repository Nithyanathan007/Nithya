from models import get_user

def verify_user(username, password):
    stored_password = get_user(username)
    if stored_password and stored_password == password:
        return {"message" : "Login successful!"}
    return {"status" : "Invalid credentials"}