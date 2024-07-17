from add import add
from minus import minus
from multiply import multiply
from divede import divede

a = int(input("a: "))
b = int(input("b: "))

command = input('add, multiply, minus, divide: ')

if command == 'add':
    print(add(a, b))

elif command == 'multiply':
    multiply(a, b)

elif command == "minus":
    minus(a, b)

elif command == "divede":
    divede(a, b)