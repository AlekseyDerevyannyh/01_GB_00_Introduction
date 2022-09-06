# Сортировка методом выбора (поиском максимума)

from os import system
system("cls")

array = [3, 2, 7, -3, 0, 2, 8, 1]
arraySize = 8
tmp = 0

j = arraySize

while j > 1:
	i = 1
	iMax = 0
	while i < j:
		if array[i] > array[iMax]: iMax = i
		i += 1
	tmp = array[iMax]
	array[iMax] = array[j - 1]
	array[j - 1] = tmp
	j -= 1
print(array)