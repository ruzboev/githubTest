
########################### 1 ##########################

# reports = [(100000, "Income"),
#            (120000, "Income"),
#            (303000, "Outcome"),
#            (110000, "Income")]
""" 1 """

# new_dict = {}
# for value, key in reports:
#     if key in new_dict:
#       new_dict[key].append(value)
#     else:
#         new_dict[key] = [value]
# print(new_dict)

""" 2 """

# def add_income(incomes):
#     if "Income" in new_dict:
#       new_dict["Income"].append(incomes)
#     else:
#         new_dict["Income"] = [incomes]
#
# incomes = 5000
# add_income(incomes)
# print(new_dict)


""" 3 """

# def add_outcome(outcome):
#     if "Outcome" in new_dict:
#       new_dict["Outcome"].append(outcome)
#     else:
#         new_dict["Outcome"] = [outcome]
#
# outcome = 555000
# add_outcome(outcome)
# print(new_dict)

""" 4 """
# def calculate_report(new_dict):
#     a = sum(new_dict["Income"])
#     b = sum(new_dict["Outcome"])
#     print(f'foyda {a}, chiqim {b}, zarar {a-b}')
#
#
# calculate_report(new_dict)

########################### 2 ##########################


users = {
    	"ali": {"first_name": "Alibek", "last_name": "Valiyev", "password": "ali123$", "more_info": "more_info"},
    	"aziz": {"first_name": "Azizbek", "last_name": "Samadov", "password": "aziz098@", "more_info": "more_info"},
    	"humoyun": {"first_name": "Humoyun", "last_name": "Valiyev", "password": "humo123!", "more_info": "more_info"},
}

command = input('sing in or sing out ? : ')

if command == "sing in":
	...
elif command == "sing out":
	username = input('username: ')
	password = input('password: ')
else:
	print("There is no this kind of command")


