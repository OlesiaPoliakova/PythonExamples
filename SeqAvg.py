
count = 0
sum = 0
while True:
    number = int(input())
    sum += number
    count += 1
    if number == 0:
        break
print(sum//count)


"""Определите среднее значение всех элементов последовательности, завершающейся числом 0"""