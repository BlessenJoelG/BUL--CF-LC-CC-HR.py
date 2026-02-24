t = int(input())
for a in range(t):
    alpha = str()
    x = input()
    x = list(x)
    x[0],x[4] = x[4],x[0]
    for _ in x:
        alpha = alpha + _
    print(alpha)