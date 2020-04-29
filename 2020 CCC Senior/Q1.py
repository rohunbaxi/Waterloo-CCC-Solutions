import math
n = int(input())

speeds = list()
for x in range(n):
    speeds.append(list(map(int, input().split(' '))))

speeds.sort()
minSpeed = math.fabs((speeds[1][1] - speeds[0][1]) / (speeds[1][0] - speeds[0][0]))

checkSpeed = 0
for x in range(2, n):
    checkSpeed = math.fabs((speeds[x][1] - speeds[x-1][1]) / (speeds[x][0] - speeds[x-1][0]))
    if checkSpeed > minSpeed:
        minSpeed = checkSpeed

print(minSpeed)

    
