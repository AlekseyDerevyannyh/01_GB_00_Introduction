# Нахождение индексов максимального и минимального элементов массива

from os import system
system("cls")

array = [1, -2, 3, 9, 5, 6]
arraySize = 6

iMin = 0
iMax = 0
i = 0

while i < arraySize:
	if array[i] < array[iMin]: iMin = i
	if array[i] > array[iMax]: iMax = i
	i += 1
print(iMin, iMax)