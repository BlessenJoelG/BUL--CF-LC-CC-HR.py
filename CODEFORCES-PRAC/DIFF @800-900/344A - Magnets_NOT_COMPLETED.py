val,magnets_row = 0,[]
n = int(input())
for _ in range(n):
    magnets_row.append(int(input()))
if n == 1:
    val = 1
elif n==2 and magnets_row[0] != magnets_row[0+1]:
    val =  2
else:
    for x in range((len(magnets_row))-1):
        if magnets_row[x] == magnets_row[x + 1]:
            val = val + 1
print(val)