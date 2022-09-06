# # 1 week days
# day = int(input('Введите день недели:'))
# work_days = {1: 'понедельник', 2: 'вторник', 3: 'среда', 4: 'четверг', 5: 'пятница'}
# holidays = {6: 'суббота', 7: 'воскресенье'}
# if day in work_days:
#     print(f'Это рабочий день - {work_days[day]}')
# elif day in holidays:
#     print(f'Это выходной день - {holidays[day]}')
# else:
#     print(f'Это неправильный день - {day} , введите от 1 до 7 день .')

# Task 2
# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# arr = [
#     [True, True, True],
#     [True, True, False],
#     [True, False, False],
#     [False, False, False],
#     [False, True, True],
#     [False, False, True],
#     [False, True, True],
# ]
#
# for row in arr:
#     x, y, z = row
#
#     print("----------------------")
#
#     print("x = " + str(x))
#     print("y = " + str(y))
#     print("z = " + str(z))
#
#     leftResult = not (x and y and z)
#     rightResult = not x or not y or not z
#
#     print("----------------------")
#
#     print(f"leftResult = {str(leftResult)} rigthResult = {str(rightResult)}")
#     print("Равны ?  -> " + str(leftResult == rightResult))
#     print("----------------------")
#     print("----------------------")

# Task 3
# x = int(input('Введите X: '))
# y = int(input('Введите Y: '))
# if x == 0 and y == 0:
#     print(f'X ({x}) и Y ({y}) не должны равняться нулю!')
# system_part_coordinate = None
# if x > 0 and y > 0:
#     system_part_coordinate = 1
# if x < 0 and y > 0:
#     system_part_coordinate = 2
# if x < 0 and y < 0:
#     system_part_coordinate = 3
# if x > 1 and y < 0:
#     system_part_coordinate = 4
# print(f'X = {x} , Y = {y}  => четверть - {system_part_coordinate}')

# Task 4
# coordinate = int(input('Введите четверть: '))
# match coordinate:
#     case 1:
#         print(f'Вы ввели четверть {coordinate}. Координаты  x > 0 and y > 0.')
#     case 2:
#         print(f'Вы ввели четверть {coordinate}. Координаты  x < 0 and y > 0.')
#     case 3:
#         print(f'Вы ввели четверть {coordinate}. Координаты  x < 0 and y < 0.')
#     case 4:
#         print(f'Вы ввели четверть {coordinate}. Координаты  x > 1 and y < 0.')
#     case _:
#         print(f'Вы ввели не правильную четверть координат {coordinate}')

# Task 5
# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
x1 = float(input('введите X1 -'))
y1 = float(input('введите Y1 -'))
x2 = float(input('введите X2 -'))
y2 = float(input('введите Y2 -'))

x = (x1 - x2) ** 2
y = (y1 - y2) ** 2
print(x, y)
z = x + y
sgrt = round(z ** (0.5), 2)
print(sgrt)
