import math


def distance(x1, y1, x2, y2):
    s = math.sqrt((x2-x1)**(x2-x1) + (y2-y1)**(y2-y1))
    return s


print('Расстояние от первой точки до второй равно {}'. format(distance(3, 2, 4, 5)))


def power(a, n):
    result = 1
    for i in range(abs(n)):
        result *= a
    return result if n >= 0 else (1 / result)


print('a в степени n равно {}'.format(power(2, 3)))


def capitalize(str):
    return ' '.join([word.capitalize() for word in str.split(' ')])


print('Строка со словами с большой буквы')
print(capitalize('opra winfrey the best tv presentor'))


def capitalize1(str):
    s = ' '.join(word[0].upper() + word[1:] for word in str.split())
    return s


print(capitalize1('opra winfrey the best tv presentor'))
