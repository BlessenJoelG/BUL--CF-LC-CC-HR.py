t = int(input())
for _ in range(t):
    x,c = [input().strip(".")for i in range(8)],""
    for _ in x:
        c = c + _
    print(c)