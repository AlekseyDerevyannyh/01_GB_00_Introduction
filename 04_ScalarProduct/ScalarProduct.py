# Скалярное произведение двух векторов

from os import system
system("cls")

vector1 = [1, 1, 1, 1]
vector2 = [1, 1, 1, 1]
vectorSize = 4

i = 0
scalarProduct = 0

while i < vectorSize:
	scalarProduct += vector1[i] * vector2[i]
	i +=1
print(scalarProduct)