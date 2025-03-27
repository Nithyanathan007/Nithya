users_db = {
    "admin": "password123",
    "user1": "mypassword"
}

def get_user(username):
    return users_db.get(username)