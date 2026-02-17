tot_dol=0
k,n,w = map(int,input().split())
for i in range(w+1):
    tot_dol = tot_dol + (i*k)
if tot_dol <= n:
    tot_dol = 0
    print(tot_dol)
else:
    print(tot_dol-n)
