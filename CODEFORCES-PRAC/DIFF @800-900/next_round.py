nxro = 0
partici = []
n,k = map(int,input().split(" "))
partici = list(map(int,input().split(" ")))
for x in partici:
    if x>0:
        if (x >= partici[k-1]):
            nxro = nxro + 1
print(nxro)