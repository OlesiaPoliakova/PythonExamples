count = 0
prev_number = None
while True:
    number = int(input())
    if prev_number is not None and prev_number < number:
        count += 1
    if number == 0:
        break
    prev_number = number
print(count)


"""Последовательность состоит из натуральных чисел и завершается числом 0. 
Определите, сколько элементов этой последовательности больше предыдущего элемента"""