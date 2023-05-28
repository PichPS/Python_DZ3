# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5
# import random

n = int(input("Введите кол-во элементов в массиве: "))
list_n = [int(i) for i in input('Перечислите n чисел: ').split()] 
arr = list(map(int, list_n))
# arr = []
x = int (input("Введите число x: "))
# for i in range(n):
#     arr. append()
#     # arr.append(random.randrange(n))
# print(arr)
def nearval(arr, number):
    return min(arr, key=lambda x: abs(number - abs(x))) 
print("->", nearval(arr, x))