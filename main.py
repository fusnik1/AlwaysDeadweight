myMonitorDiagonal = 21.5
monitorRatio = 27/myMonitorDiagonal
useRatio = True


while(True):
	userInput = input("Get Launch Angle (Distance/<EnemyDirection>/Wind/<WindDirection>): ")
	distanceString = userInput.split("/")[0]
	enemyDirection = userInput.split("/")[1]
	windspeedString = userInput.split("/")[2]
	windDirection = userInput.split("/")[3]
	distance = float(distanceString)
	windspeed = float(windspeedString)
	if (useRatio):
		if (windDirection == enemyDirection):
			angle = 90 - (distance/1.05*monitorRatio - windspeed/14)
			print()
			print(angle)
			print()
		elif (windDirection != enemyDirection):
			angle = 90 - (distance/1.05*monitorRatio + windspeed/14)
			print()
			print(angle)
			print()
		else:
			print()
			print("you fucked up the syntax try again")
			print()
	else:
		if (windDirection == enemyDirection):
			angle = 90 - (distance/1.05 - windspeed/14)
			print()
			print(angle)
			print()
		elif (windDirection != enemyDirection):
			angle = 90 - (distance/1.05 + windspeed/14)
			print()
			print(angle)
			print()
		else:
			print()
			print("you fucked up the syntax try again")
			print()
