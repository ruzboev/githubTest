
####################################### 1 ########################################

"""  1  """
# def my_list(int_list):
#     list1 = [i for i in int_list if i % 3==0]
#     return list1
#
# int_list = [2, 4, 6, 8, 7, 9, 10]
# print(my_list(int_list))

"""  2  """

# int_list = [2, 4, 6, 8, 7, 9, 10]
# list_comprehension = list(filter(lambda i: i % 3 ==0, int_list))
# print(list_comprehension)

####################################### 2 ########################################

"""  1  """

# def my_list(int_list):
#     list1 = sum[i**2 for i in int_list]
#     return list1
#
# int_list = [2, 4, 6, 8, 7, 9, 10]
# print(my_list(int_list))

"""  2  """

# def my_list(int_list):
#     new_list = sum(map(lambda i: i**2, int_list))
#
#     return new_list
#
# int_list = [2, 4, 6, 8, 7, 9, 10]
# print(my_list(int_list))


####################################### 3 ########################################

"""  1  """
# def my_list(str_list):
#     return list(len(val) for val in str_list )
#
# str_list = ["This", "is", "a", "sample", "sentence"]
# print(my_list(str_list))


"""  2  """

# def my_list(str_list):
#
#     new_list = map(lambda i: len(i), str_list)
#
#     return list(new_list)
#
# str_list = ["This", "is", "a", "sample", "sentence"]
# print(my_list(str_list))


####################################### 4 ########################################

"""  1  """

# def last_vowel(str_list):
#     vowels = ["i", "o", "e", "y", "a", 'u']
#     return list(filter(lambda s: s[-1] in vowels, str_list))
#
# str_list = ["Mike", "Emma", "Kelly", "Brad"]
#
# print(last_vowel(str_list))

"""  2  """
# def last_vowel(str_list):
#     vowels = ["i", "o", "e", "y", "a", 'u']
#     return [s for s in str_list if s[-1] in vowels]
#
#
# str_list = ["Mike", "Emma", "Kelly", "Brad"]
# print(last_vowel(str_list))


####################################### 5 ########################################
"""  1  """

# def bal_list(ave_bal):
#      return [sum(val)//len(val) for val in ave_bal]
#
# ave_bal = [[60, 70, 80, 90, 100, 66], [50, 55, 65, 75, 85, 90], [70, 75, 80, 85, 90, 95]]
# print(bal_list(ave_bal))

"""  2  """
# def bal_list(ave_bal):
#     return list(map(lambda val: sum(val)//len(val), ave_bal))
#
#
#
# ave_bal = [[60, 70, 80, 90, 100, 66], [50, 55, 65, 75, 85, 90], [70, 75, 80, 85, 90, 95]]
# print(bal_list(ave_bal))

####################################### 6 ########################################
"""  1  """
# def per_product(value):
#     return list(map(lambda val: int(val*0.90), value))
#
#
# value = [6000, 7000, 8000, 9000, 10000, 6600]
# print(per_product(value))



"""  2  """

# def per_product(value):
#     return list(int(val*0.90) for val in value )
#
#
# value = [6000, 7000, 8000, 9000, 10000, 6600]
# print(per_product(value))



####################################### BONUS - 7 ########################################
"""  1  """

# def my_num(num_list):
#     juft = [val**2 for val in num_list if val % 2 ==0 and val**3 for val in num_list if val % 3 ==0]
#     return juft
# num_list = list(range(1,100))
# print(my_num(num_list))

"""  2  """

# def my_num(num_list):
#     juft = list(map(lambda val: val**2, filter(lambda val: val % 2 == 0, num_list)))
#     toq = list(map(lambda val: val**3, filter(lambda val: val % 3 == 0, num_list)))
#     return juft, toq
#
# num_list = list(range(1, 100))
# print(my_num(num_list))