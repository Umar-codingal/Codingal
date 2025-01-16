import random
import time

def getRandom(startDate,endDate):
    print("Printing ranom date between", startDate, "and", endDate)
    generateRandom= random.random()
    dateFormat = "%m/%d/%Y"

    startTime=time.mktime(time.strptime(startDate, dateFormat))
    endTime= time.mktime(time.strptime(endDate, dateFormat))

    randomTime= startTime + generateRandom * (endTime-startTime)
    randomDate = time.strftime(dateFormat,time.localtime(randomTime))

    return randomDate

print("Random date", getRandom("1/1/2016","12/1/2018"))