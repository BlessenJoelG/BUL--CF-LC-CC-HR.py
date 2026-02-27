t = int(input())
for _ in range(t):
    x = int(input())
    x = str(x)
    if len(x)>2 and  x.startswith("10") and x[2]!="0" and int(x[2:])>=2:
        print("YES")
    else:
        print("NO")