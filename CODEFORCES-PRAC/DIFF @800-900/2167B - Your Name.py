t= int(input())
for i in range(t):
    s_t = []
    n = int(input())
    s_t.extend(map(str,input().split()))
    s = [_ for _ in s_t[0]]
    s.sort()
    t = [_ for _ in s_t[1]]
    t.sort()
    if s == t:
        print("YES")
    else:
        print("NO")
    s.clear()
    t.clear()