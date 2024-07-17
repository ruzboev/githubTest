import os

users = {
   "ali": {"first_name": "Alibek", "last_name": "Valiyev", "password": "ali123$", "more_info": "more_info"},
   "aziz": {"first_name": "Azizbek", "last_name": "Samadov", "password": "aziz098@", "more_info": "more_info"},
   "humoyun": {"first_name": "Humoyun", "last_name": "Valiyev", "password": "humo123!", "more_info": "more_info"},
}

""" 1- usul """
# def file_handel(file):
#    ...
# my_file = ...
#
# res = file_handel()

"""
mode
r => read => read(), readline(), readlines()
w => write => ichidigi info ochirib, yengisini yozadi, yengi file xam yaratadi
a => append => qoshadi
r+ => read and write === birinchi oqidi  keyin qoshib yozadi
w+ => write and read === birinchi ochiradi keyin yozadi + oqidi
"""



# with open('file/data.txt', mode='r') as my_file:
   # print(my_file)
   # print(type(my_file))
   # info = my_file.read()
   # info1 = my_file.readline()
   # info2 = my_file.readline()
   # info3 = my_file.readline()
   # print(info1)
   # print(info2)
   # print(info3)

   # info1 = my_file.readlines()
   # for line in info1:
      # print(line.split('\n')[0])
      # print(line.rstrip())
#
# with open('file/new.txt', mode='a') as my_file:
#    my_file.write('smth\n')
#    my_file.write('smth1\n')
#    my_file.write('smth2\n')
#    my_file.write('smth3\n')
#
#
# with open('file/new.txt', mode='r') as readable_file:
#    print(readable_file.read())


# import os
# print(dir(os))
#
# my_path = os.getcwd()
# print(my_path)
#
# new_file_path = 'text.txt'
# file_path = os.path.join(my_path, new_file_path)
# print(file_path)
#
# with open(new_file_path, 'w') as test_file:
#    test_file.write('test test')
#
# if os.path.exists(file_path):
#    print('bor')

# with open('file/new.txt', mode='r+') as readable_file:
#     print(readable_file.read())
#     readable_file.write('yangi\n')
#     print(readable_file.read())


# with open('file/11_add.txt', mode='w+') as file:
#    file.write('465454')
#    # file.seek(0)
#    file.write('sanjar\n')
#    file.write('san')
#    file.seek(0)         # kursortni boshiga obkeladi boshidan oqish uchun
#    print(file.tell())    # kursort qata turganini bilib beradi
#    print(file.read())
#

''' 2- usuli '''

# my_file = open('file/new.txt', 'r')
#
#
# print(my_file.read())
#
# my_file.close()


# import os
# os.rename('file/new.txt','file/abc.txt')
#
# deleted_files = ['file/new5.txt', 'file/yangi.txt', 'file/SAM.txt']
# # os.remove('file/new5.txt')
#
# my_path = os.getcwd()
#
# for file in deleted_files:
#    # os.remove(file)
#    os.remove(os.path.join(my_path, file))
#



def get_info(file):
    with open(file, 'r') as my_files:
        first_name, last_name, age, *others = my_files.readlines()

        print(f'ismi {first_name.rstrip()}, familya {last_name.rstrip()}, yoshi {int(age.rstrip())}')


get_info('11_add.txt')