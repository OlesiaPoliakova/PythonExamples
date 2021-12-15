
count = 0
sum = 0
while True:
    number = int(input())
    sum += number
    count += 1
    if number == 0:
        break
print(sum/count)

# from statistics import mean
#
# def input_integers_till_zero():
#     while (x := int(input())) != 0:
#         yield x
#     yield x

print(f'Average is : {mean(input_integers_till_zero())}')
"""Определите среднее значение всех элементов последовательности, завершающейся числом 0"""