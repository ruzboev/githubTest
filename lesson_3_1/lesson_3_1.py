# import re
#
def validate_email(email):
    """Check if the provided email has a valid format."""
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def register_user():
    """Register a new user by collecting email, password, first name, and last name."""
    users = {}

    # Prompt for email and validate the format
    email = input("Enter your email: ")
    while not validate_email(email):
        print("Invalid email format. Please try again.")
        email = input("Enter your email: ")

    # Prompt for other user details
    password = input("Enter your password: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    # Save user details in the dictionary
    users[email] = {
        "password": password,
        "first_name": first_name,
        "last_name": last_name
    }

    print("User registered successfully!")
    return users

# Register a user and print the details
registered_users = register_user()
print(registered_users)