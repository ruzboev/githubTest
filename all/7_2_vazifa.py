            ########################### 1 ########################

# def my_list(list1, list2):
#     a = set(list1).isdisjoint(set(list2))
#     return a
#
# list1 = [2, 3, 4, 5]
# list2 = [4, 5, 6, 7]
# print(my_list(list1, list2))

            ########################### 2 ########################

# def sett(set1, set2):
#     a = set1.intersection(set2)
#     b = set1.difference(a)
#     return b
#
#
# set1 = {2, 3, 4, 5}
# set2 = {4, 5, 6, 7}
# print(sett(set1, set2))

        ########################### 3 ########################
# def sett(set1, set2):
#     diff = set2-set1
#     return diff
#
#
# set1 = {1, 2, 3, 4, 5}
# set2 = {9, 10, 4, 5, 6, 7}
# print(sett(set1, set2))

        ########################### 4 ########################

employees = {
"Alice": {"Python", "Java"},
"Bob": {"JavaScript", "HTML"},
"Charlie": {"Python", "JavaScript"}
}

""" 1 """
# def new_skill(emp, skill):
#     a = employees[emp]
#     a.add(skill)
#     print(a)
#
#
# emp = input('name: ')
# skill = input('skill: ')
# print(new_skill(emp, skill))

""" 2 """
# def new_skill(emp, skill):
#
#     if skill in employees[emp]:
#         a = employees[emp]
#         a.remove(skill)
#         return a
#     else:
#         return "Bunday skill yo’q"
#
#
# emp = input('name: ')
# skill = input('skill: ')
# print(new_skill(emp, skill))

""" 3 """

# def new_skill(emp):
#
#     a = employees[emp]
#
#     return a
#
#
# emp = input('name: ')
# print(new_skill(emp))


            ########################### 5 ########################

# def intersection(list1, list2, list3):
#     a = set(list1).intersection(set(list2), set(list3))
#     return a
#
#
# list1 = [1, 6, 3, 4, 5]
# list2 = [4, 5, 6, 7, 1]
# list3 = [7, 8, 6, 1]
# print(intersection(list1, list2, list3))
