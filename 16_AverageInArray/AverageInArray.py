# Среднее арифметическое всех элементов массива

from os import system
system ("cls")

array = [2, 2, 20, 20]
arraySize = 4

average = 0
i = 0

while i < arraySize:
	average += array[i]
	i += 1
average /= arraySize
print(average)