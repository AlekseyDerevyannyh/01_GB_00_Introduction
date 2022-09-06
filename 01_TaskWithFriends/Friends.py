# Два друга идут навстречу друг другу, а между ними бегает собака.
# Сколько раз собака перебежит от одного друга к другому, пока они не встретятся?

from os import system
system("cls")

firstFriendSpeed = 1
secondFriendSpeed = 2
dogSpeed = 5
distance = 10000
distanceMin = 10
friend = 2

count = 0
distanceBetweenFriends = distance
while distanceBetweenFriends > distanceMin:
	if friend == 2:
		timeToMeet = distanceBetweenFriends / (secondFriendSpeed + dogSpeed)
		friend = 1
	else:
		timeToMeet = distanceBetweenFriends / (firstFriendSpeed + dogSpeed)
		friend = 2
	distanceBetweenFriends = distanceBetweenFriends - timeToMeet * (firstFriendSpeed + secondFriendSpeed)
	count = count + 1
print (count)
