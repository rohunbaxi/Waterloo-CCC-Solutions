jersey = int(input())
count = 0
for a in range(1, jersey):
    for b in range((a+1), jersey):
        for c in range((b+1), jersey):
            count+=1

print(count)
