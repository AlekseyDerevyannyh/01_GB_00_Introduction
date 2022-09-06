# Найти сумму элементов массива, лежащих между максимальным
# и минимальным по значению элементами

from os import system
system ("cls")

array = [6, 2, 1, 4, 3, 8, 7]
arraySize = 7

sum = 0
iMax = 0
iMin = 0
i = 1

while i < arraySize:
	if array[i] < array[iMin]: iMin = i
	if array[i] > array[iMax]: iMax = i
	i += 1
if iMin < iMax:
	i = iMin + 1
	while i < iMax:
		sum += array[i]
		i += 1
else:
	i = iMax + 1
	while i < iMin:
		sum += array[i]
		i += 1
print(sum)
