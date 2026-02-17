w = 0
frd = []
n,h = map(int,input().split())
frd = map(int,input().split())
frdx = list(frd)
for x in range(n):
    if frdx[x] <= h:
        w = w+1
    else:
        w = w+2
print(w)