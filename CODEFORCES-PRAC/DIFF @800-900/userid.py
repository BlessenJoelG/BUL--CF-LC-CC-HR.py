usid = input()
freq = [[0]for i in range(len(usid))]
for i in range (len(usid)):
    tar = usid[i]
    for x in range (len(usid)):
        freq[x] = usid.count(usid[x])
print(freq)