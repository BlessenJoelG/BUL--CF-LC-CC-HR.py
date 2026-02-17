val_1,val_0 = 0,0
n = int(input())
x = list(map(int,input().split()))
for _ in range(len(x)):
    if x[_] == 1:
        val_1 = val_1+1
if val_1>=1 and val_1<=100 :
    print("HARD")
else:
    print("EASY")
