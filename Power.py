a = float
def power(a, n):
    result = 1
    for i in range(abs(n)):
        result *= a
    return result if n >= 0 else (1 / result)


# print('a в степени n равно {}'.format(power(2, 3)))