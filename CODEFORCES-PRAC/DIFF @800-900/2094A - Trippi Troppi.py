t = int(input())
for i in range(t):
    x,c = [],""
    x = input().split(" ")
    for _ in x:
        c = c + _[0]
print(c)