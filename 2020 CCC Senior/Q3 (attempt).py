needle = input()

haystack = input()


taken1 = list()
def permutations(a):

    letters = list()
    for x in range(len(a)):
        letters.append(a[x])
    strings = list()
    for i in range(len(letters)):
        for x in range(len(letters)):
            if x != i:
                for q in range(len(letters)):
                    if q != x and q != i:
                        string = letters[i] + letters[x] + letters[q]

                        checkTaken1 = False
                        for t in range(len(taken1)):
                            if string == taken1[t]:
                                checkTaken1 = True
                            

                        if checkTaken1 == False:
                            strings.append(string)
                            taken1.append(string)
    return strings


perms = permutations(needle)

lenPerm = len(perms[0])

taken = list()

COUNTER = 0

checkList = list()

for x in range(len(haystack)):
    check = ''
    for q in range(x, x + lenPerm):
        if x + lenPerm <= len(haystack):
            check += haystack[q]
                
    for o in range(len(perms)):
        if perms[o] == check:
            checkTaken = False

            for t in range(len(taken)):
                if check == taken[t]:
                    checkTaken = True

            if checkTaken == False:
                COUNTER += 1
                taken.append(check)

print(COUNTER)

