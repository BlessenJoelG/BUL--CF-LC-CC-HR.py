opr = []
x = 0
n = int(input())
if(1<=n<=150):
    for i in range(n):
        opr.append(input())
    for indx in (opr):
        if indx in ("x++","++x"):
            x = x+1
        if indx in ("x--","--x"):
            x = x-1
print(x)