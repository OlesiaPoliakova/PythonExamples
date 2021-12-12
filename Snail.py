h = int(input()) #длина шеста
a = int(input()) #ползет вверх за день
b = int(input()) #спускается вниз за ночь
# always a>b
time = ((h-a)//(a-b))+1
print(int(time))

""" 
edge cases
10 3 2
10 5 2
10 2 1
10 9 1
"""

