# Вычислить число c заданной точностью d Пример: при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
n = 3.1415926535
d = float(input('Введите число: '))

if 10 ** -1 >= d >= 10 ** -10:
    r = round(n, 3)
    print(r)
else:
    print(f'Число  {d} задано не верно')

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input())
list_simple = []
simple = 2
while num > 1:
    if num % simple == 0:
        list_simple.append(simple)
        num = num / simple
    else:
        simple += 1
print(list_simple)

# Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.

a = [15, 23, 4, 7, 43, 11, 4]
b = []

for index, i in enumerate(a):
    doublicate = False
    for index_2, j in enumerate(a):
        if index == index_2:
            continue
        if i == j:
            doublicate = True
    if not doublicate:
        b.append(i)

print(b)
