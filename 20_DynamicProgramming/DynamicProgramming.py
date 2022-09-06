# У исполнителя Калькулятор две команды, которым присвоены номера:
#	1. прибавь 1
#	2. умножь на 4
# Сколько есть программ, которые число 1 преобразуют в число 55?

from os import system
system ("cls")

numbers = [0] * 56
numbers[0] = 1
numbers[1] = 1
count = 2

while count < 56:
	if (count % 4) == 0:
		numbers[count] = numbers[count // 4] + numbers[count - 1]
	else:
		numbers[count] = numbers[count - 1]
	print(count, numbers[count])
	count += 1