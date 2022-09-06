# Найти сумму всех элементов массива с нечётными индексами

from os import system
system("cls")

array = [1, 2, 3, 4, 5, 6]
arraySize = 6

sumOdd = 0
i = 1

while i < arraySize:
	sumOdd += array[i]
	i += 2
print(sumOdd)