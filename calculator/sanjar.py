#                     #"""1-Savol"""
#
# # print()
# #
# # x = int(input('4 xonali son kiriting: '))
# #
# # print()
# # # 4567
# #
# # a = x%10*1000
# # b = x//10%10*100
# # c = x//100%10*10
# # d = x//1000
# #
# # print(f'4 xonali son teskarisi: {a+b+c+d}')
#
#
#                     #"""2-Savol"""
# #
# # a = 70000
# # b = 6
# # c = 0.35
# # d = 0.65
# # n = a*b
# # print()
# # print(f'xizmat uchun xaq: {n}')
# # e = int(n*c)
# # print()
# # print(f'ustani ish xaqi: {e}')
# # f = int(n*d)
# # print()
# # print(f'kompaniya ulushi: {f}')
#
# #
# # #                         #"""3-savol"""
# #
# # a = int(input("3 xonali son kiriting: "))
# #
# # b = a % 10
# # c = a //10%10
# # d = a //100
# #
# # e = b**3+c**3+d**3
# # print()
# # print(e)
# # print()
# # if e==a:
# #     print('True')
# # else:
# #     print('False')
# #
# #
# #
# #                     #"""4-savol"""
# #
# # soat = 2
# # minut = 0
# # print()
# # kelgan_soat = int(input('soat nechada keldi: '))
# # print()
# # kelgan_minut = int(input('nechada minutda keldi: '))
# # print()
# #
# # a = kelgan_soat-soat
# # b = kelgan_minut-minut
# # if kelgan_soat>soat and kelgan_minut>minut:
# #     print(f'{a} soat {b} minutga kechikdi')
# #
# # elif kelgan_soat<=soat and kelgan_minut>=minut:
# #     print("vaqtida keldi")
# #
# # elif kelgan_soat==soat and kelgan_minut==minut:
# #     print("vaqtida keldi")
# #
# # elif kelgan_soat<soat and kelgan_minut>minut:
# #     print("vaqtida keldi")
# #
# # else:
# #     ...
#
# #                     #"""5-savol"""
# #
# # list = [9,6,17,24,28,101,238,457,496,6452,8128]
# # a=1
# # for i in list:
# #     y=0
# #     for a in  range(1,i):
# #         if i%a==0:
# #             y+=a
# #     if y == i:
# #         y+=i
# # print(y)
#
#
# def check_string(my_str, char):
#     ...
# my_string = input("a:")
# char = input("b:")
# check_string(my_string, char)
#
# # char my_string ichida/ ichida emas
#
# # if char in my_string:
# #     return('true')
# # else:
# #     print("false")
#



# def my_str(list1):
#     a = ' '.join(list1)
#     return a
#
#
#
#
#
# list1 = ['hello', 'word']
# print(my_str(list1))

# products = [('olma', 5),('anor', 2),('nok', 7),('ananas', 3)]
# def pro(products):
#
#     a = sorted(products, key=lambda x: x[1])
#
#     return a
#
#
# print(pro(products))


# def skidka(*pro):
#     x, *y = pro
#     a = sum(y)
#     return a * (100 - x) / 100
#
#
# pro = [10, 1000, 2000, 3000]
# print(skidka(10, 1000, 2000, 3000))


# def my_list(list1, list2):
#
#     a = list1+list2
#     b = sorted(a, key=lambda s: s)
#
#     return b
#
#
# list1 = [5, 3, 4, 2]
# list2 = [10, 7, 16, 6]
# print(my_list(list1, list2))







