x = input()

romans = []
for i in range(len(x)):
    if i % 2 == 1:
        romans.append(x[i])

for q in range(len(romans)):
    if romans[q] == 'I':
        romans[q] = 1
    elif romans[q] == 'V':
        romans[q] = 5
    elif romans[q] == 'X':
        romans[q] = 10
    elif romans[q] == 'L':
        romans[q] = 50
    elif romans[q] == 'C':
        romans[q] = 100
    elif romans[q] == 'D':
        romans[q] = 500
    elif romans[q] == 'M':
        romans[q] = 1000

SubtractIndex = []

for z in range(1, len(romans)):
    if romans[z] > romans[z - 1]:
        SubtractIndex.append(z-1)

AROMATIC = 0

for y in range(len(SubtractIndex)):
    AROMATIC -= 2*int(x[2 * SubtractIndex[y]])*romans[SubtractIndex[y]]

for a in range(int(len(x)/2)):
    AROMATIC += int(x[2*a]) * romans[a]

print(AROMATIC)
