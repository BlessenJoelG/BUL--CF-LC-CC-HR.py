n = int(input())
s = []
for i in range(n):
    s.append(input())
for x in s:
    leng = len(x) - 2
    if len(x)>10:
        print(x[0]+str(leng)+x[-1])
    else:
        print(x)