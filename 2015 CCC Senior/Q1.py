x = int(input())
table = list()
for i in range(x):
  table.append(list(map(int,input().split(" "))))

Sum = 0

RealNumbers = list()

for q in range(len(table)):
    if table[q][0] == 0:
        del RealNumbers[len(RealNumbers)-1:]
    else:
        RealNumbers.append(table[q][0])
for z in range(len(RealNumbers)):
    Sum += RealNumbers[z]

print(Sum)

