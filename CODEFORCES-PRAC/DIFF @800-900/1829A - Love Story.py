chk_list = ["c","o","d","e","f","o","r","c","e","s"]
t = int(input())
for _ in range(t):
    x = input()
    c = 0
    for a in range(len(x)):
        if x[a]!= chk_list[a]:
            c = c+1
    print(c)