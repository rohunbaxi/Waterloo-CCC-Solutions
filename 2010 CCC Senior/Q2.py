#HuffmanEncoding

chrs = int(input())

codes = list()
for x in range(chrs):
    codes.append(list(map(str, input().split(' '))))

seq = input()

maxL = 0
for x in range(len(codes)):
    if len(codes[x][1]) > maxL:
        maxL = len(codes[x][1])

maxL = maxL +1

output = ''
while (len(seq)) > 0:
    for i in range(maxL + 1):
        for u in range(len(codes)):
            if str(seq[0:(i+1)]) == codes[u][1]:
                output += codes[u][0]
                seq = seq[(len(codes[u][1])):]

print(output)
