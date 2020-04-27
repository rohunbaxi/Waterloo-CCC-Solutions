x = input()
questions = int(x)

table = []
for i in range(2*questions):
  table.append(list(map(str,input().split(" "))))

correct = 0

for q in range(questions):
    if table[q][0] == table[q+questions][0]:
        correct += 1

print(correct)
