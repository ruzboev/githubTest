""" 1 """
# def sum_integers(data):
#     integers = []
#     for val in data:
#         if isinstance(val, int):
#             integers.append(val)
#
#     if not integers:
#         raise ValueError("No integers found in the input data")
#     return sum(integers)
#
# try:
#     data = [1, 'a', 3.14, 5, 'b', 7]
#     result = sum_integers(data)
#     print("Sum of integers:", result)
# except ValueError as e:
#     print("Error:", e)


""" 2 """

# import os
# import csv
#
# def read_csv_file(sanjar):
#     try:
#         with open(sanjar, 'r') as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 print(row)
#     except FileNotFoundError:
#         print(f"Error: The file '{sanjar}' was not found.")
#
# sanjar = "sanjar"
#
# read_csv_file(sanjar)


""" 3 """

import csv

# def exists_email(email):
#     try:
#         with open("contacts.csv", 'r', encoding='utf-8') as csvfile:
#             content = csv.reader(csvfile, delimiter='|')
#             for row in content:
#                 csv_email = row[1].strip()  # strip spaces from email
#                 if csv_email == email:
#                     return True
#     except FileNotFoundError:
#         # Handle the case where the file does not exist yet
#         return False
#     return False
#


# def email_check(email):
#     try:
#         if '@mail' not in email:
#             print("Invalid email.")
#             return False
#         return True
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return False
#
# def number_check(phone_number):
#     try:
#         if not phone_number.startswith('+998'):
#             print("Wrong Code")
#             return False
#         return True
#
#         number_check(phone_number)
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return False
#
#
# def user():
#     try:
#         full_name = input("Full name: ")
#         email = input("Email: ")
#         phone_number = input("Phone number: ")
#
#         if email_check(email) and number_check(phone_number):
#             print("Registration successful!")
#         else:
#             print("Registration failed due to invalid email or phone number.")
#
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# user()
#
#