# import json
# from pprint import pprint
#
# import requests
#
# requests.get()
# requests.post()
#
# dict -> json json.dumps(indent=4)
# json -> dict json.loads()
# lst = [1, 4, 4.6, '5', 'abc', [1, 2, 3]]
#
#
# def sum_nums(lst: list) -> int:
#     summ = 0
#     for item in lst:
#         try:
#             a = float(item)
#         except (ValueError, TypeError) as e:
#             ...
#         else:
#             summ += a
#
#     return summ
#
#
# print(sum_nums(lst))
#
# # print(int('5'))
#
#
#
# url = 'https://jsonplaceholder.typicode.com/todos'
#
# content = requests.get(url)
#
# content_json = content.json()[:20]
#
# print(type(content_json))
#
# # pprint(content.json()[:20])
#
# reversed_content = sorted(content_json, key=lambda n: n['id'], reverse=True)
# # pprint(reversed_content)
#
# completed_todos = [completed_todo for completed_todo in content_json if completed_todo['completed']]
#
# uncompleted_todos = [uncompleted_todo for uncompleted_todo in content_json if not uncompleted_todo['completed']]
#
# pprint(completed_todos)
# pprint(uncompleted_todos)
#
# Paradigm => OOP, FP, PP
#
# ismi
# familiyasi
# role
# maosh
# yoshi
# contact
# task
#
# employees_list = [
#     {
#         "ismi": ...
#     },
#     {},
#     {},
# ]
#
#
# OOP => class va object
#
# Employee -> class
# employee -> object
#
# def dlklds_ldjf()
#
# class HPComputer:
#     model = "HP"
#     def __init__(self):
#         ...
#
#
# class NTEmployee:
#     workplace = "NT"
#
#     def __init__(self, first_name, last_name, phone, salary):
#         # print('init ....')
#         self.ism = first_name
#         self.last_name = last_name
#         self.phone = phone
#         self.salary = salary
#
#     def calculate_salary(self, tip):
#         return self.salary * (100 + tip) / 100
#
#     def full_name(self):
#         return f"{self.ism} {self.last_name}"
#
#     def update_phone(self, new_phone):
#         self.phone = new_phone
#         print('Updated phone')
#
#
# employee_1 = NTEmployee('Anvar', 'sdl', '901234567', 1000)
# employee_2 = NTEmployee('Dilshod', 'dsldsklfskl', '901234567', 2000)
#
# print(employee_1.phone)
# employee_1.update_phone("991234567")
# print(employee_1.phone)
#
#
# # print(employee_1.calculate_salary(20))
# # print(employee_1.full_name())
# # print(employee_2.full_name())
# #
# # # print(employee_1.ism)
# # print(employee_2.workplace)
# # print(employee_1.workplace)
#
# #
# # class Cars:
# #     def __init__(self, model, nomi, rangi, narxi):
# #         self.model = model
# #         self.nomi = nomi
# #         self.rangi = rangi
# #         self.narxi = narxi
# #
# #     def __str__(self):
# #         return f"{self.nomi} nomli mashina. rangi {self.rangi} ....."
# #
# #
# # cobalt_car = Cars('chev', 'Cobalt', 'oq', 100_000)
# # spark_car = Cars('chev', 'Spark', 'qora', 70_000)
# #
# #
# # print(cobalt_car)
# # print(spark_car)
#
# """
# model: chev, nomi: Cobalt, rangi: oq, narxi: 100 ml
# model: chev, nomi: Spark, rangi: qora, narxi: 80 ml
# model: chev, nomi: Spark, rangi: qora, narxi: 80 ml
# model: chev, nomi: Spark, rangi: qora, narxi: 80 ml
# model: chev, nomi: Spark, rangi: qora, narxi: 80 ml
# """
#
# # class HPComputer:
# #     model = "HP"
# #     ...
#
# """
# attribute: model(brand), name, rangi, cpu, ssd, ram
# method: calculate(), ...
# """
#
# """
# property => model, nomi, rangi, ... == attribute
# behavour => yuradi, toxtaydi  == method
# """
#
# """
# attribute => 1) class 2)instance
# """