M = int(input())
N = int(input())

gridList = list()

for i in range(M):
    gridList.append(list(map(int, input().split(' '))))

def findfactors(a):
    factors = list()
    for x in range(1, (M+1)):
        check = False
        for i in range(1, (N+1)):
            if (x * i) == a and check == False:
                addList = [x,i]
                factors.append(addList)
                check = True
    return factors


overallCheck = False

v1 = gridList[0][0]
toss = findfactors(v1)
if M*N == v1:
    overallCheck = True

for x in range((M*N)+ 1):
    newList = list()
    for i in range(len(toss)):
        v2 = gridList[toss[i][0] - 1][toss[i][1] - 1]
        if M*N == v2:
            overallCheck = True

        toss2 = findfactors(v2)
        for q in range(len(toss2)):
            newList.append(toss2[q])
    toss = newList

if overallCheck == True:
    print('yes')
else:
    print('no')
