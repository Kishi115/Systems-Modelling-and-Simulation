import random
from tabulate import tabulate

# no. of arrivals
n = 100000

# column headers
interval = [random.randint(0, 10)]
arriveTime = [1]
waitTime = [0]
timeAtServe = [1]
serveTime = [random.randint(1, 5)]
departTime = [timeAtServe[0] + serveTime[0]]
queueLine = [0]

# average wait and departure times, and average queue length
avW = [0]
avD = [departTime[0]]
avQ = [0]

table = []

sumW = 0
sumD = departTime[0]
sumQ = 0

for x in range(1, n):
    interval.append(random.randint(0, 10)) 
    arriveTime.append(arriveTime[x-1] + interval[x])
    waitTime.append(max(0, departTime[x-1] - arriveTime[x]))
    timeAtServe.append(arriveTime[x] + waitTime[x])    
    serveTime.append(random.randint(1, 5))
    departTime.append(timeAtServe[x] + serveTime[x])

    
    # minus index of first person who departed after current arrival
    # from index of current arrival
    for y in range(0, x + 1):
        if(departTime[y] > arriveTime[x]):
            queueLine.append(x - y)
            break
    sumW = sumW + waitTime[x]
    sumD = sumD + departTime[x]
    sumQ = sumQ + queueLine[x]
    avW.append(sumW/x)
    avD.append(sumD/x)
    avQ.append(sumQ/x)
    
      
  # formatting into ascii table
for x in range(n):
    table.append([interval[x], arriveTime[x], waitTime[x], timeAtServe[x], serveTime[x], departTime[x], queueLine[x], avW[x], avD[x], avQ[x]])

print (tabulate(table, headers=["i", "at", "wt", "tas", "st", "dt", "ql", "avW", "avD", "avQ"]))
