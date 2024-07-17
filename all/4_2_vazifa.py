
########################### 1 #####################
'''1'''

# str_list = ['asd', 'sdfg', 'tyui', 'dfgda']
#
# def str_a(str_list):
#     a = filter(lambda s: 'a' in s, str_list)
#
#     return list(a)
#
# print(str_a(str_list))

'''2'''

#
# def str_a(str_list):
#     a = map(lambda s: 'a' in s, str_list)
#
#     return list(a)
#
# print(str_a(str_list))


######################### 2 #####################

# str_list = ['asd', 'sdfgs', 'tyui', 'dfgd']
#
# def str_a(str_list):
#     a = (val for val in str_list if val[0]==val[-1])
#
#     return list(a)
#
# print(str_a(str_list))

######################### 3 #####################

# str_list = [1, 2, 3, -5, -7, -9]
#
# def str_a(str_list):
#     a = filter(lambda s: s > 0, str_list)
#
#     return list(a)
#
# print(str_a(str_list))

######################### 4 #####################

# strings = ['hello123', 'world', 'python!', 'programming', '123', 'code']
#
#
# def my_str(strings):
#
#     a = filter(lambda x: x.isalpha(), strings)
#     return list(a)
#
#
# print(my_str(strings))


######################### 5 #####################

# strings = ['hello123', 'world', 'python!', 'programming', '123', 'code']
#
#
# def capital_letter(strings):
#     a = ' '.join(map(lambda x: x.capitalize(), strings))
#
#     return a
#
#
# print(capital_letter(strings))

######################### 6 #####################

# strings = ['world', 'programming', 'hello', 'world']
#
#
# def len_str(strings):
#
#     a = map(lambda x: len(x), strings)
#     return list(a)
#
#
# print(len_str(strings))

######################### 6-bonus #####################

# palindrom_list = ["deed", "peep", "wow", "noon", "Walter", "Brian"]
#
#
# def new_list(palindrom_list):
#     a = filter(lambda s: s == s[::-1], palindrom_list)
#     return list(a)
#
#
# print(new_list(palindrom_list))


######################### 7-bonus #####################

# Berilgan sonlar ichidan tublarini chiqaruvchi dastur yozing(filter orqali)


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True
#
#
# def priem_new_list(prime_list):
#
#     prime_num = list(filter(is_prime, prime_list))
#     return prime_num
#
#
# prime_list = [2, 3, 4, 5, 8, 9, 10]
# print(priem_new_list(prime_list))


######################### 8-bonus #####################

# def index_list(tuple_list):
#     empty = []
#     for i in tuple_list:
#         a = tuple_list.index(i)
#         empty.append(a)
#     return empty
#
#
# tuple_list = (2, 3, 4, 5, 8, 9, 10)
# print(index_list(tuple_list))
