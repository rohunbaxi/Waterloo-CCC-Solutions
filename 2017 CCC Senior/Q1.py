n = int(input())
table = []
for i in range(2):
  table.append(list(map(int,input().split(" "))))
  
N = len(table[0])

sumX = 0
sumY = 0

z = False
i = 0

check = 0
while i < N:
    x = table[0][i]
    y = table[1][i]
    sumX += x
    sumY += y

    if sumX == sumY:
        z = True
        check = i 
    i += 1
if z == True:
    print(check+1)

if z == False:
    print(0)
