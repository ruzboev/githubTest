from users_info import users
def update_password():
    def update_pass(username, new_pass):
        if username in users:
            users[username]["password"] = new_pass
            return "Password updated successfully"
        else:
            return 'Incorrect username'


    username = input('Username: ')
    old_password = input('Old password: ')
    if username in users and old_password == users[username]["password"]:
        new_password = input('New password: ')
        print(update_pass(username, new_password))
        print(users)
    else:
        print("Incorrect username or password")