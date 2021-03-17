# JWT --> Json Web Token 
from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
    # user = username_mapping.get(username,None)
    user = UserModel.find_by_username(username)
    print("*"*10)
    print(user)
    print("*"*10)
    if user and user.password == password:
        print("returning user")
        return user

def identity(payload):
    user_id = payload["identity"]
    print("%"*10)
    print("user id")
    print("%"*10)
    return UserModel.find_by_id(user_id)
