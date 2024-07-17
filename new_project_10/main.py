
from users_info import users
from sign_up import register_user
from sign_in import login
from update_pass import update_password

command = input('sign in or register or change password ? : ')
if command == "register":
	register_user()

elif command == "sign in":
	login()

elif command == "change password":
	update_password()

else:
	print("There is no this kind of command")
