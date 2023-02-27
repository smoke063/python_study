import re

# 1. Напишите функцию read_last(lines, file), которая будет открывать определенный файл file 
# и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число). Протестируем функцию на файле «article.txt» со следующим содержимым:


def read_last(lines, file):
    with open(file, "r", encoding="utf8") as f:
        print(f.readlines()[lines:])

# read_last(3, 'article.txt')

# Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).
def longest_words(file):
    with open(file, "r", encoding="utf8") as f:
        content = f.read().split()
        lenMax = len(max(content, key=len))
        print(list(filter(lambda x: len(x) == lenMax, content)))
longest_words('article.txt')
