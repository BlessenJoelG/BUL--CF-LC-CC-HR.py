t =int(input())
for x in range(t):
    n,a,m,b,c = int(input()),input(),int(input()),input(),input()
    x,y = "",""
    for _ in range(len(c)-1,-1,-1):
        if c[_] == "V":
            x = x + b[_]
    for _ in range(len(c)):
        if c[_] == "D":
            y = y + b[_]
    print(x+a+y)
