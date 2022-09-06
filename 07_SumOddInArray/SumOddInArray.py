# Найти сумму всех элементов массива с нечётным значением. 
# Например, для массива [1, 2, 4, 6] ответ будет 1, т.к. здесь у нас только один нечётный элемент

from os import system
system("cls")

array = [1, 2, 4, 6, 7]
arraySize = 5

sumOdd = 0
i = 0

while i < arraySize:
	if array[i]%2 == 1: sumOdd += array[i]
	i += 1
print(sumOdd)