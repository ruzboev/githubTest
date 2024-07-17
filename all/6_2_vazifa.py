                          ########################### 1 ########################

""" 1 """

word = "pneumonoultramicroscopicsilicovolcanoconiosis"

my_dict = {}

for char in word:
    if char in my_dict:
        my_dict[char] += 1
    else:
        my_dict[char] = 1

print(my_dict)

                          ########################### 2 ########################
#
# students = [("Alice", "A"), ("Bob", "B"), ("Charlie", "A"), ("David", "C"), ("Eve", "B")]
#
# class_dict = {}
#
# for student in students:
#     name, grade = student
#     if grade not in class_dict:
#         class_dict[grade] = []
#     class_dict[grade].append(name)
#
# print(class_dict)
                          ########################### 3 ########################

# users = {
#   1: {"name": "Alice", "age": 30, "email": "alice@example.com"},
#   2: {"name": "Bob", "age": 25, "email": "bob@example.com"},
# }
#
#
# def user1(user2):
#     if user2 in users:
#         user = users[user2]
#         return f"User named {user['name']}. He is {user['age']} years old. He can be reached at {user['email']}"
#
#     else:
#         return "Topilmadi"
#
#
# user2 = int(input("ID: "))
# print(user1(user2))


                          ########################### 4 ########################


# Dict comprehension orqali bajaring.
# 1 dan n gacha (n ni o’zi ham kiradi) sonlarni factorialini hisoblab yozing:
# {1: 1, 2: 2, 3: 6, 4: 24, 5: 120, ….}

# n = int(input("num: "))
#
# import math
#
# factorials = {i: math.factorial(i) for i in range(1, n + 1)}
#
# print(factorials)



                          ########################### 5 ########################
""" 1 """
#
# product_prices = {
#   "Apple": 5,
#    "Banana": 3,
#    "Orange": 7
# }
#
#
# def get_product_price(product_name):
#     if product_name in product_prices:
#         return product_prices[product_name]
#     else:
#         return "Bu mahsulot yo\'q"
#
# product_name = input("product_name: ")
# print(get_product_price(product_name))

""" 2 """

# product_prices = {
#   "Apple": 5,
#    "Banana": 3,
#    "Orange": 7
# }
#
# def add_product(new_product, price):
#
#     if new_product not in product_prices:
#
#         product_prices[new_product] = int(price)
#         return product_prices
#     else:
#         return "bu mahsulot mavjud"
#
#
# new_product = input("product_name: ")
# price = input("product_price: ")
# print(add_product(new_product, price))


""" 3 """
# product_prices = {
#   "Apple": 5,
#    "Banana": 3,
#    "Orange": 7
# }
#
# def calculate_price(product_name, quantity):
#
#     if product_name in product_prices:
#         price = quantity * product_prices[product_name]
#         return f'Total price: {price}'
#     else:
#         return "bu mahsulot mavjud emas"
#
#
# product_name = input("product_name: ")
# quantity = int(input("product_quantity: "))
# print(calculate_price(product_name, quantity))

                          ########################### Bonus 6 ########################



                          ########################### Bonus 7 ########################

# n = int(input("num: "))
#
# numbers = {num: (num**2 if num % 2 == 0 else num**3) for num in range(1, n + 1)}
#
# print(numbers)

