# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

val = [2, 3, 5, 9, 3]
array_find = []

for index, value in enumerate(val):
    if index % 2 != 0:
        array_find.append(value)
print(sum(array_find))

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
#  Пример: - [2, 3, 4, 5, 6] => [12, 15, 16]; - [2, 3, 5, 6] => [12, 15]

val = [2, 3, 4, 5, 6]
array_find = []

mid = round(len(val) / 2 + 0.5)
for index, value in enumerate(val):
    if mid == index:
        break
    else:
        array_find.append(value * val[-1 if index == 0 else (index + 1) * -1])
print(array_find)

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

val = [1.1, 1.2, 3.1, 5, 10.01]
array_find = []

val_1 = list(map(lambda x: round(x % 1, 3), val))
val_1 = list(filter(lambda x: x != 0, val_1))
print(val_1)
max_v = max(val_1)
min_v = min(val_1)
print(max_v - min_v)

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: - 45 -> 101101 ;  3 -> 11 ; 2 -> 10
i = int(input('Введите десятичное число: '))

print(f'Десятичное число {i} = двоичному числу {bin(i)}')

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# k = 8

k = 8


def fib(k):
    if k in [1, 2]:
        return 1
    elif k in [0]:
        return 0
    else:
        return fib(k - 1) + fib(k - 2)


res_2 = []
for e in range(0, k + 1):
    res_2.append(fib(e))
print(res_2)


def fib(k):
    if k in [-1, -2]:
        return -1
    else:
        return fib(k + 1) + fib(k + 2)


res_1 = []
for e in range((-1) * k, 0):
    res_1.append(fib(e))
print(res_1)

print(res_1 + res_2)
