N = int(input())

positions = list()
for x in range(N):
    positions.append(int(input()))

positions = positions[0:]
positions.sort()

smallestSize = 10000000000000000000000000000000000000

i = 1
while i < len(positions) - 1:
  nh =(int(positions[i+1])-int(positions[i]))/ 2
  xh = (int(positions[i])- int(positions[i-1]))/2
  nh += xh
  i += 1
  if nh < smallestSize:
    smallestSize = nh

print(round(smallestSize,1))

