# Программа, которая переносит самое большое значение элемента в правый край массива
# Реализация с попарным сравнением элементов и перестановкой большего вправо

from os import system
system("cls")

array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
arraySize = 9

tmp = 0
i = 0
while i < (arraySize - 1):
	if array[i] > array[i + 1]:
		tmp = array[i]
		array[i] = array[i + 1]
		array[i + 1] = tmp
	i += 1
print(array)