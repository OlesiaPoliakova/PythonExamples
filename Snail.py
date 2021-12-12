import math
h = int(input()) #длина шеста
a = int(input()) #ползет вверх за день
b = int(input()) #спускается вниз за ночь
# always a>b

if a >= h:
    time = 1
else:
    time = 1 + math.ceil((h-a)/(a-b))
print(int(time))
""" 
edge cases
10 3 2
10 5 2
10 2 1
10 9 1
10 6 1
10 11 1
"""
"""
 неправильное округление 
кейсы не работают 
10 6 1
10 11 1 
h = int(input()) #длина шеста
a = int(input()) #ползет вверх за день
b = int(input()) #спускается вниз за ночь
# always a>b
time = ((h-a)//(a-b))+1
print(int(time))"""
