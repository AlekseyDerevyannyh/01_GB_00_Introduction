# Сортировка массива методом пузырька

from os import system
system("cls")

# array = [3, 2, 7, -3, 0, 2, 8, 1]
array = [8, 7, 6, 5, 4, 3, 2, 1]
arraySize = 8

tmp = 0
j = arraySize - 1
while j > 0:
	i = 0
	while i < j:
		if array[i] > array[i + 1]:
			tmp = array[i]
			array[i] = array[i + 1]
			array[i + 1] = tmp
#		print(i, j, array)
		i += 1
	j -= 1
print(array)