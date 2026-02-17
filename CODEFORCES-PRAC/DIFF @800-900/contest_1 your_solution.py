d_list = []
z = 0
g = []
t = int(input())
for _ in range(t):
    g.append(int(input()))
for y in range(1,10**9):
    d_y = str(y)
for _ in range(len(d_y)):
    d_list.append((map(int,d_y[_])))
    for _ in range(len(d_list)):
        z = z+d_list[_]
    if y - z == g[_]:
        c = c+1
print(c)