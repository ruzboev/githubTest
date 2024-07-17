def validate_email(email):
    if "@" in email and "." in email:
        return True
    return False


def validate_password(password):
    if len(password) < 8:
        return False
    return True


def register_user():
    user_data = {}

    email = input("Enter your email: ")
    while not validate_email(email):
        print("Invalid email format. Please try again.")
        email = input("Enter your email: ")

    password = input("Enter your password: ")
    while not validate_password(password):
        print("Password too short. Please enter at least 8 characters.")
        password = input("Enter your password: ")

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    user_data['email'] = email
    user_data['password'] = password
    user_data['first_name'] = first_name
    user_data['last_name'] = last_name

    print("Registration successful!")
    return user_data


user = register_user()
print("User data:", user)