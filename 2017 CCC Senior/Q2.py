n = int(input())
table = []
for i in range(1):
  table.append(list(map(int,input().split(" "))))
table[0].sort()
waves = table[0]
import math
N = len(waves)

ORDER = list()

if N%2 == 0:
    index = int(N/2)
    lowWaves = waves[:index]

    highWaves = waves[index:]
    lowWaves.sort(reverse = True)

    i = 0
    while i < (N/2):
        ORDER.append(lowWaves[i])
        ORDER.append(highWaves[i])

        i += 1
else:
    index = int(math.ceil(N/2))
    lowWaves = waves[:index]
    highWaves = waves[index:]

    lowWaves.sort(reverse = True)
    i = 0
    while i < (index - 1):
        ORDER.append(lowWaves[i])
        ORDER.append(highWaves[i])

        i += 1
    ORDER.append(lowWaves[i])

print(" ".join(str(x) for x in ORDER))
