#######################  1  ######################

# def multiply_even(list1):
#     a=1
#     for val in list1:
#         if val % 2 ==0:
#              a *= val
#     return a
#
#
# list1 = [1, 2, 3, 4, 5, 6]
# print(multiply_even(list1))

#######################  2  ######################

'''with max'''

# def find_max(list):
#     return max(list)
#
# list = [10, 15, 11, 16, 80, -1]
# print(find_max(list))

'''without max'''
#
# def find_max(numbers):
#     max_num = numbers[0]
#
#     for num in numbers:
#         if num > max_num:
#             max_num = num
#
#     return max_num
#
# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# print(find_max(numbers))

#######################  3  ######################

''' 1 '''
# def my_list(str):
#     empty = []
#     for val in str:
#         if len(val) > 5:
#             empty.append(val)
#     return empty
#
# str = ['asdfa12', 'asd555', '12dfg', 'ab']
# print(my_list(str))

''' 2 '''

# def my_list(str):
#     empty = []
#     for val in str:
#         if len(val) > 5:
#             str.remove(val)
#     return val
#
# str = ['asdfa12', 'asd555', '12dfg', 'ab']
# print(my_list(str))

#######################  4  ######################

# def my_list(list1):
#     empty = []
#     for val in list1:
#         if val != '':
#             empty.append(val)
#
#     return empty
#
# list1 = ['mike', '', 'elma', 'kelly', '', 'brad']
# print(my_list(list1))


#######################  5  ######################

# def list1(list2):
#     new_list = []
#     a = 1
#     for i in list2:
#         a = i**3
#         new_list.append(a)
#     return new_list
#
# list2 = [1, 2, 3, 4]
# print(list1(list2))

#######################  6  ######################

# def new_list(old_list):
#     new_list1 = []
#     count_dict = {}
#     for i in old_list:
#         if i in count_dict:
#             count_dict[i] += 1
#         else:
#             count_dict[i] = 1
#         new_list1.append(count_dict.copy())
#     return new_list1
#
# old_list = ['a', 'b', 'a', 'c', 'd', 'a', 'b', 'b']
# print(new_list(old_list))


users = {
   "ali": {"first_name": "Alibek", "last_name": "Valiyev", "password": "ali123$", "more_info": "more_info"},
   "aziz": {"first_name": "Azizbek", "last_name": "Samadov", "password": "aziz098@", "more_info": "more_info"},
   "humoyun": {"first_name": "Humoyun", "last_name": "Valiyev", "password": "humo123!", "more_info": "more_info"},
}

print(users["ali"]["password"])