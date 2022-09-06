# Разворот массива

from os import system
system("cls")

array = [1, 2, 3, 4]
arraySize = 4
tmp = 0

i = 0
while i < (arraySize / 2):
	tmp = array[arraySize - i - 1]
	array[arraySize - i - 1] = array[i]
	array[i] = tmp
	i += 1
print (array)