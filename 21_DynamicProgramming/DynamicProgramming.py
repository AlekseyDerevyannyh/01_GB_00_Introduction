# У исполнителя Калькулятор три команды, которым присвоены номера:
#	1. прибавь 1
#	2. умножь на 2
#	3. умножь на 3
# Сколько есть программ, которые число 1 преобразуют в число 18

from os import system
system ("cls")

numbers = [0] * 19
numbers[0] = 1
numbers[1] = 1
count = 2

print (1, 1)
while count < 19:
	if ((count % 2) == 0) & ((count % 3) == 0):
		numbers[count] = numbers[count // 2] + numbers[count // 3] + numbers[count - 1]
	elif ((count % 2) == 0) & ((count % 3) != 0):
		numbers[count] = numbers [count // 2] + numbers[count - 1]
	elif ((count % 2) != 0) & ((count % 3) == 0):
		numbers[count] = numbers[count // 3] + numbers[count - 1]
	else:
		numbers[count] = numbers[count - 1]
	print(count, numbers[count])
	count += 1