# Все 5-буквенные слова, составленные из букв А, К, Р, У, записаны в алфавитном порядке.
# Вот начало списка:
#	1. ААААА
#	2. ААААК
#	3. ААААР
#	4. ААААУ
#	5. АААКА
#	...
# Запишите слово, которое стоит на 350-м месте от начала списка

from os import system
system ("cls")

l = ['А', 'К', 'Р', 'У']
k = 0
for el1 in l:
	for el2 in l:
		for el3 in l:
			for el4 in l:
				for el5 in l:
					k = k + 1
					if k == 350: print (k, el1, el2, el3, el4, el5)