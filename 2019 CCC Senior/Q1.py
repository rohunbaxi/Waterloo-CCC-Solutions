#Flipper

command = input()

orientation = [1,2,3,4]

for x in range(len(command)):
    if command[x] == 'V':
        copy = orientation[1]
        orientation[1] = orientation[0]
        orientation[0] = copy

        copy = orientation[3]
        orientation[3] = orientation[2]
        orientation[2] = copy
    else:
        copy1 = orientation[1]
        orientation[1] = orientation[3]
        orientation[3] = copy1

        copy1 = orientation[0]
        orientation[0] = orientation[2]
        orientation[2] = copy1

print(str(orientation[0]) + ' ' + str(orientation[1]) + '\n' + str(orientation[2])+ ' ' + str(orientation[3]))
