# Нахождение максимального и минимального элементов массива

from os import system
system("cls")

array = [1, 10, 3, 4, -5]
arraySize = 5

iMin = 0
iMax = 0
i = 1

while i < arraySize:
	if array[i] < array[iMin]: iMin = i
	if array[i] > array[iMax]: iMax = i
	i += 1
print(array[iMin], array[iMax])