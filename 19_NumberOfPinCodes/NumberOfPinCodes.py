# Найти количество пинкодов из трёх знаков, где первым элементом могут быть все
# буквы латинского алфавита, а двумя остальными цифры

from os import system
system ("cls")

l1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
l2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
i = 0
for el1 in l1:
	for el2 in l1:
		for el3 in l2:
			i = i + 1
			print (i, el1, el2, el3)
for el1 in l1:
	for el2 in l2:
		for el3 in l1:
			i = i + 1
			print (i, el1, el2, el3)
for el1 in l2:
	for el2 in l1:
		for el3 in l1:
			i = i + 1
			print (i, el1, el2, el3)