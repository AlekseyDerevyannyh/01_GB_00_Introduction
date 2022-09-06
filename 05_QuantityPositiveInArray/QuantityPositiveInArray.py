# Посчитать количество положительных чисел в произвольно заданном массиве

from os import system
system("cls")

array = [-1, -1 , 3, 7, -8]
arraySize = 5

quantityPositive = 0
i = 0

while i < arraySize:
	if array[i] > 0: quantityPositive += 1
	i += 1
print (quantityPositive)