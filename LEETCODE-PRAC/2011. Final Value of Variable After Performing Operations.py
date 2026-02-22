s,c = [],0
s.extend(map(str,input().split()))
for _ in range (len(s)):
    if s[_] == "X++" or s[_] == "++X":
        c = c+1
    else:
        c = c-1
print(c)