string ='Hello, there are eggs and spam'
x = ''
for i in range(len(string)): #1 version
    if i % 3:
        x += string[i]
print(x)

x = ''
"""Дана строка. Удалите из нее все символы, чьи индексы делятся на 3."""
for i, char in enumerate(string): #2 version
    if i % 3:
        x += char
print(x)
