def remove_element(data, k):
    for i in range(k, len(data)-1):
        data[i] = data[i+1]
        print(data)
    data.pop()
    print(data)


remove_element([1, 3, 5, 7, 9, 10], 2)

# data = [1, 3, 5, 7, 9, 10]
# k = int(input())
#
# for i in data:
#     data.remove(data[k])
#     print(data)
# data.pop()
# print(data)


def increasing_neighbours(data):  # 1 version

    for i in range(len(data)-1):
        if data[i] < data[i+1]:
            print(data[i+1])


increasing_neighbours([1, 3, 5, 7, 9, 10])

""" Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента."""


def maximal_element(data):
    maximum = 0
    max_index = 0
    for i, number in enumerate(data):
        if number > maximum:
            maximum = number
            max_index = i

    print(maximum)
    print(max_index)


maximal_element([1, 3, 5, 7, 9, 10])
""" Дан список чисел. Выведите значение наибольшего элемента в списке, 
а затем индекс этого элемента в списке. Если наибольших элементов несколько, 
выведите индекс первого из них."""


def find_max_index(data):
    max_index = 0
    maximum = 0
    for i, number in enumerate(data):
        if number > maximum:
            maximum = number
            max_index = i
    return max_index


find_max_index([1, 3, 5, 7, 9, 10, 11, 233])


def find_min_index(data):
    min_index = 0
    minimum = 0
    for i, number in enumerate(data):
        if number < minimum:
            minimum = number
            min_index = i
    return min_index


find_min_index([1, 3, 5, 7, 9, 10, 11, 233])


def swap_min_and_max(data):
    max_index = find_max_index(data)
    min_index = find_min_index(data)
    min_index = max_index
    print(min_index)


swap_min_and_max([1, 3, 5, 7, 9, 10, 11, 233])

""" В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка. """
