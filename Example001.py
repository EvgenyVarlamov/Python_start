# print('hello word')

# Типы данных и переменные ###############################################################
# # int, float, boolen, str, list, None
# # value = None
# a = 123
# b = 1.23
# # print(type(a))
# # print(type(b))
# # print(a)
# # print(b)
# # value = 12345
# # print(type(value))
# s = 'hello world'  # \n - переход на новую строку
# print(s)  # вывод строки
# print(a, '-', b, '-', s)
# print('{} - {} - {}'.format(a, b, s))    # вывод по порядку
# print('{1} - {2} - {0}'.format(a, b, s))  # изменение порядка вывода
# print(f'{a} - {b} - {s}')  # интерполяция

# f = True
# print(f)

# list = ['1', '2', '3']
# col = ['1', '2', '3', 'hello world', 1, 2, 4.5, True]
# print(list)
# print(col)

# Ввод и вывод ##################################################################################
# print, input

# print('Введите a') # строковые input()
# a = input()
# print('Введите b')
# b = input()
# print(a, b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')
# print(a, '+', b, '=', a+b)

# print('Введите c') # целочисленные int(input())
# c = int(input())
# print('Введите d')
# d = int(input())
# print(c, '+', d, '=', c+d)

# print('Введите e') # вещественные float(input())
# e = float(input())
# print('Введите f')
# f = float(input())
# print(e, '+', f, '=', e+f)

# Арифметические операции ############################################################################
# +, -, *, /, //, **

# a = 123
# b = 321
# c = a+b
# print(c)

# a = +123 # унарный плюс
# b = -321 # унарный минус
# c = a+b
# print(c)

# a = 2
# b = 8
# c = a-b
# print(c)

# a = 2
# b = 8
# c = a*b
# print(c)

# a = 2
# b = 8
# c = a/b # обычное деление
# print(c)

# a = 12
# b = 5
# c = a//b  # деление в целых числах
# print(c)

# a = 12
# b = 8
# c = a % b  # остаток от деления
# print(c)

# a = 2
# b = 8
# c = a ** b  # возведение в степень
# print(c)

# a = 1.3
# b = 3
# c = a * b
# print(c)

# a = 1.3
# b = 3
# c = round(a * b)
# print(c)

# a = 1.3123123
# b = 3
# c = round(a * b, 7)
# print(c)

# a = 3
# a = a+5
# print(a) # 8

# a = 3
# a += 5  # сокращенная операция 3+5
# print(a)  # 8

# a = 3
# a *= 5  # сокращенная операция 3*5
# print(a)  # 15


# Логические операции ###############################################################
# >, >=, <, <=, ==, !=
# not, and, or -не путать с &, |, ^
# is, is not, in, not in
# gen

# a = 1 > 4
# print(a) # False

# a = 1 < 4
# print(a)  # True

# a = 1 < 4 and 5 > 2
# print(a)  # True

# a = 1 == 2
# print(a)  # False

# a = 1 != 2
# print(a)  # True

# a = 'qwe'
# b = 'qwe'
# print(a == b)  # True

# a = [1, 2]
# b = [1, 2]
# print(a == b)  # True

# a = 1 < 3 < 5 < 10
# print(a)  # True

# func = 1
# T = 4
# x = 123
# print(func < T > (x))  # False

# func = 1
# T = 4
# x = 2
# print(func < T > (x))  # True

# f = 1 > 2 or 4 < 6
# print(f)  # True

# f = [1, 2, 3, 4]
# print(f)
# print(2 in f)  # True

# f = [1, 2, 3, 4]
# print(f)
# print(not 2 in f)  # False

# f = [1, 2, 3, 4]
# is_odd = f[0] % 2 == 0
# print(is_odd)  # False

# f = [1, 2, 3, 4]
# is_odd = not f[0] % 2
# print(is_odd)  # False

# Управляющие конструкции ###############################################################
# if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША')
# elif username == 'Марина':
#     print('Я так ждал Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет,', username)

# while

# original = 2345
# inverted = 0
# while original != 0:
#     inverted = inverted*10+(original % 10)
#     original //= 10
# print(inverted)

# while-else

# original = 2345
# inverted = 0
# while original != 0:
#     inverted = inverted*10+(original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит)')
# print(inverted)

# for

# for i in 1, 2, 3, 4, 5:
#     print(i**2)

# list = [1, 2, 3, 4, 10, 5]
# for i in list:
#     print(i**2)

# r = range(10)
# for i in r:
#     print(i)

# for i in range(5):
#     print(i)

# for i in range(1, 5):
#     print(i)

# for i in range(1, 10, 3):
#     print(i)

# for i in 'qwe-rty':
#     print(i)

# Строки ###############################################################

# text = 'съешь ещё этих мягких французских булок'
# help(text.istitle)
# print(len(text))                    # 39
# print('ещё' in text)                # True
# print(text.isdigit())               # False
# print(text.islower())               # True
# print(text.replace('ещё', 'ЕЩЁ'))
# for c in text:
#     print(c)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0])
# print(text[1])
# # print(text[len(text)])
# print(text[len(text)-1])
# print(text[-5])
# print(text[:])
# print(text[:])
# print(text[len(text)-2:])
# print(text[2:9])
# print(text[6:-18])
# print(text[0:len(text):6])
# print(text[::6])
# text = text[2:9] + text[-5] + text[:2]

# Списки ###############################################################
# list = list

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))
# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)
# for i in numbers:
#     i *= 2
#     print(i)
# print(numbers)

# colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e)          # red green blue

# for e in colors:
#     print(e*2)        # redred greengreen blueblue

# colors.append('gray')  # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray'])
# colors.remove('red')  # del colors[0]  # удалить элемент
# print(colors)

# Функции ###############################################################
# def

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return


arg = 1
print(f(arg))
print(type(f(arg)))