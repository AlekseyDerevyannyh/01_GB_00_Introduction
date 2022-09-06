# Поиск второго максимального элемента в массиве

from os import system
system ("cls")

numbers = [9, 8, 3, 2, 6]
size = 5
currentIndex = 0
maxNumberIndex = 0
max = numbers[0]
secondMax = 0
while currentIndex < size:
	if numbers[currentIndex] > max:
		max = numbers[currentIndex]
		maxNumberIndex = currentIndex
	currentIndex += 1
currentIndex = 0
secondMax = numbers[0]
if maxNumberIndex == 0:
	secondMax = numbers[1]
while currentIndex < size:
	if currentIndex != maxNumberIndex:
		if numbers[currentIndex] > secondMax:
			secondMax = numbers[currentIndex]
	currentIndex += 1
print(secondMax)