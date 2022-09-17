# 1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: - 6782 -> 23; - 0,56 -> 11

a = input("Введите число: ")


def func(arr):
    summ = 0
    for i in arr:
        if i.isdigit():  # пытается преобразует строку в число
            summ += int(i)
    return summ


print(func(a))

# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример: - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input("Введите число: "))


def f(n: int):
    i = 0
    arr = []
    while i < n:
        if i == 0:
            arr.append(1)
        else:
            arr.append(arr[i - 1] * (i + 1))
        i += 1
    return arr


print(f(N))

# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

N = 6


def f(n: int):
    i = 1
    dict = {}
    while i <= n:
        if i == 1:
            dict[i] = i + 3
        else:
            dict[i] = dict[i - 1] + 3
        i += 1
    return dict


print(f(N))

# 4
N = 5

l = list(range(N * -1, N))

f = open("dz24.txt", "r")

positions = []

for line in f.readlines():
    positions.append(int(line.rstrip('\n')))

result = None
for position in positions:
    if result is None:
        result = l[position]
    else:
        result *= l[position]

print(result)
