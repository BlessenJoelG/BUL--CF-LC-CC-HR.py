c = 0
n = int(input())
for _ in range(n):
    p,q = map(int,input().split())
    if (q-p >= 2 and q>p):
        c = c+1
print(c)