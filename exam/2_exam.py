""" 1 """
# def sum_numbers(num):
#     a = sum(num)
#     return a
#
#
# num = [1, 2, 3, 4, 5, 6, 7, 8]
# print(sum_numbers(num))


""" 2 """
# def price(product):
#     a = list(num * 0.85 for num in product)
#     return a
#
#
# product = [100, 150, 300]
# print(price(product))


""" 3 """
# def expenses(xarajatlar):
#     a = input("Oy xarajatlari: ")
#     b = xarajatlar[a]
#     return sum(b)
#
#
# xarajatlar = {
#     "yanvar": [100, 230, 150, 340],
#     "fevral": [500, 200, 27, 30],
#     "mart": [100, 120, 320, 600]}
# print(expenses(xarajatlar))


""" 4 """
users = {
"ali" : {'first_name': 'Alibek', 'last_name': 'Valiyev', 'password': 'ali123#', 'more_info': 'more_info'},
"aziz" : {'first_name': 'Azizbek', 'last_name': 'Samadov', 'password': 'aziz098@', 'more_info': 'more_info'},
"humoyun" : {'first_name': "Humoyun", "last_name": 'Valiyev', 'password': 'humo123!', 'more_info': 'more_info'}
}
def login_checker(username):
    if username in users:
        password = input('password: ')
        if password == users[username]["password"]:
            return f'{users[username]["first_name"]} {users[username]["last_name"]}  good to go'
        else:
            return "wrong password"
    else:
        return "user not found"


username = input("username: ")
print(login_checker(username))


""""""" 5 """""""

""" a """
# with open('sanjar.txt', 'a') as exam:
#     a = exam.write("sanjar ruzboev")
#     print(a)

""" b """
# with open('sanjar.txt', 'w') as exam:
#     a1 = exam.write("sanjar ruzboev\n")
#     a2 = exam.write("26\n")
#     a3 = exam.write("economics")

""" c """
# with open('sanjar.txt', 'a') as exam:
#     a1 = exam.write("\nShawn")

""" d """

import os

# os.rename('sanjar.txt', 'sanjar_ruzboev.txt')

