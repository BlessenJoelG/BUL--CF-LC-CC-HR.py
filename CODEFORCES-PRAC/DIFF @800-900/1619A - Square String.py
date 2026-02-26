t = int(input())
for _ in range(t):
    x = input()
    n = int((len(x))/2)
    if x[0:n] == x[n:]:
        print("YES")
    else:
        print("NO")