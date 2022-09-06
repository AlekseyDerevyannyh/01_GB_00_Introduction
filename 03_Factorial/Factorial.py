# Нахождение факториала

from os import system
system("cls")

number = 6

count = 1
numberFactorial = 1

while count < number:
	count += 1
	numberFactorial *= count
print ('Факториал', number, '=', numberFactorial)