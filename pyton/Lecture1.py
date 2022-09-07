from multiprocessing import Value
from re import A
from xmlrpc.client import boolean


# print('hello world')


# Типы данных справедливы
# int,float,boolean,str,list и др.

# Python - язык с динамической типизацией.
# value = 2809.
# name = 'Sergey'.

# value = None 
# a = 123 #(int)
# b = 1.23 #(float)
# print(type(a))
# print(type(b))
# value = 12345
# print(type(value))

# # s = 'hollo world'
# # print(s)
# # s = "hollo 'world"
# # print(s)
# # s = 'hollo "world'
# # print(s)
# # s = 'hollo \'world'
# # print(s)
# # s = 'hollo \nworld'

# print(s) # Вывод Строки.
# a = 123 
# b = 1.23
# s = 'hollo world'
# print(s, '-',a,'-', b)
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'[{a}, {b}, {s}]')

# f=True
# print(f)
# f=False
# print(f)

# list = [1,2,3,'Vladimir', 1.2,3,4,True]
# print (list)

# list = [1,2,3,'Vladimir',]
# col = [1.2,3,4,True]
# print (list)
# print (col)
# print('Введите A');
# a = input()
# print('Введите B');
# b = input()
# print(a, '+' ,b, '=' , a + b)
# print('{} {}'.format(a,b))
# print(f'{a} {b}')

# print('Введите A');
# a = int(input())
# print('Введите B');
# b = int(input())
# print(a, '+' ,b, '=' , a + b)

# print('Введите A');
# a =float(input())
# print('Введите B');
# b = float(input())
# print(a, '+' ,b, '=' , a + b)

# Арифметические операции
# Важно и нужно, без них вы не напишете ни одной программы
# Если помните математику – проблем не будет
# +, -, *, /, %, //, **
# Приоритет операций
# **, ⊕, ⊖, *, /, //, %, +, -
# ( ) Скобки меняют приоритет

# a = 2
# b = 4
# c = a ** b
# print(c)
# a = 1.3
# b = 3
# c = round(a * b, 2)
# print(c)
exp1 = 2**3 - 10 % 5 + 2*3 
exp2 = 2**3 - 10 / 5 + 2*3 
print(exp1)  # 14.0 или 14 
print(exp2)  # 12.0 или 12

exp1 = 2**3 - 10 % 5 + 2*3
exp2 = (2**3) - (10 / 5) + (2*3) 
print(exp1)  # 14.0 или 14 
print(exp2)  # 12.0 или 12

# Демонстрация
# Сокращённые операции и операции присваивания
# iter = 2
# iter += 3 # iter = iter + 3  
# iter -= 4 # iter = iter - 4   
# iter *= 5 # iter = iter * 5  
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5  
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5

# Демонстрация
# Дополнительно
# a, b, c = 1, 2, 3
# a: 1 b: 2 c: 3
# print('a: {} b: {} c: {}'.format(a, b, c))
# range(*(1,5,2)))

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in

# Управляющие конструкции: if, if-else
# Управляющие конструкции: 
# if, if-else Условный оператор позволяет управлять 
# ходом выполнения программы 0
