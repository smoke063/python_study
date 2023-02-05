# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# пример
# 5
# 1 2 3 4 5
# 3
# -> 1

n = int(input("Введите количество элементов в массиве: "))
arr = list(range(0, n, 1))
print(arr)
n = int(input("Введите число для поиска в массиве, его количества: "))
print(arr.count(n))

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# пример
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input("Введите количество элементов в массиве: "))
arr = list(range(1, n + 1, 1))
print(arr)
x = int(input("Введите число X для поиска в массиве самого близкого по величине элемента к числу X: "))
print(min(arr, key=lambda n: abs(x - n)))

# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:
#  A, E, I, O, U, L, N, S, T, R – 1 очко
#  D, G – 2 очка
#  B, C, M, P – 3 очка
# F, H, V, W, Y – 4 очка
# K – 5 очков
#  J, X – 8 очков
#  Q, Z – 10 очков.
#  А русские буквы оцениваются так:
#  А, В, Е, И, Н, О, Р, С, Т – 1 очко
#  Д, К, Л, М, П, У – 2 очка
#  Б, Г, Ё, Ь, Я – 3 очка
#  Й, Ы – 4 очка
#  Ж, З, Х, Ц, Ч – 5 очков
#  Ш, Э, Ю – 8 очков
#  Ф, Щ, Ъ – 10 очков.
#  Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

#  пример

#  Ввод:
#  ноутбук
#  Вывод:
#  12

word = input("Введите слово: ").lower()
scrabble = {
    1: 'авеинорст',
    2: 'дклмпу',
    3: 'бгЁья',
    4: 'йы',
    5: 'жзхцч',
    8: 'шэю',
    10: 'фщъ',
}
value = 0
for w in word:
    for k, v in scrabble.items():
      if w in v:
         value += k
      # print(f"{k} {v}")
print(f"value :  {value}")
