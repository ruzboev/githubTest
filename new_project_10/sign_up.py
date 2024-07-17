from users_info import users
def register_user():
	username = input('Username: ')
	if username in users:
		print("Username already exists. Please choose a different username.")
	else:
		first_name = input('First name: ')
		last_name = input('Last name: ')
		password = input('Password: ')
		age = input('Age: ')
		all_info = {"first_name": first_name,
					"last_name": last_name,
					"password": password,
					"age": age
					}
		users[username] = all_info
		print("User registered successfully!")
	print(users)