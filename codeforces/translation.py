s = input()
t = input()
u = ""
for i in range(1,(len(t))+1):
    u = u + t[len(t)-i]
if s == u:
    print("YES")
else:
    print("NO")
