#SR edited 2020-07-25
currentTimeStr = input("What is the current time (in hours 0-23)? ")
waitTimeStr = input("How many hours do you want to wait? ")

currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

finalTimeInt = currentTimeInt + waitTimeInt
#need to adjust time when it goes past 24
finalTimeAdjust = finalTimeInt % 24
print(finalTimeAdjust)
