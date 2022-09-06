# Программа, которая переносит самое большое значение элемента в правый край массива
# Реализация с нахождением индекса максимального элемента и последующей перестановкой с
# последним элементом

from os import system
system("cls")

array = [1, 2, 8, 3, 5]
arraySize = 5
tmp = 0

iMax = 0
i = 1

while i < arraySize:
	if array[i] > array[iMax]: iMax = i
	i += 1
tmp = array[iMax]
array[iMax] = array[arraySize - 1]
array[arraySize - 1] = tmp
print(array)