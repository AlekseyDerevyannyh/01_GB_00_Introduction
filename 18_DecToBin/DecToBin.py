# Конвертация десятичного числа в двоичное

from os import system
system ("cls")

NumberDec = int (input('N: '))
NumberBin = 0
count = 0

while NumberDec != 0:
	NumberBin = NumberBin + (10 ** count) * (NumberDec % 2)
	NumberDec = NumberDec // 2
	count = count + 1
print(NumberBin)
