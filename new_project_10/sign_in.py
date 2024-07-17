from users_info import users

def login():
    username = input('username: ')
    if username in users:
        password = input('password: ')
        if password == users[username]["password"]:
            print("Welcome to your profile", username.capitalize())
        else:
            print("Wrong password")
    else:
        print("Incorrect username")
