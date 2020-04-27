x = input()
questions = int(x)

table = []
for i in range(questions):
  table.append(list(map(str,input().split(" "))))

t = 0
s = 0
for r in range(len(table)):
    for q in range(len(table[r])):
        for z in range(len(table[r][q])):
            if table[r][q][z] == 't' or table[r][q][z] == 'T':
                t += 1
            elif table[r][q][z] == 's' or table[r][q][z] == 'S':
                s += 1
if t > s:
    print('English')
else:
    print('French')
