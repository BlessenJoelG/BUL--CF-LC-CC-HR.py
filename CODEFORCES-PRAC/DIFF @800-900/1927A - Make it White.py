t = int(input())
for i in range(t):
    size = int(input())
    x = input()
    for _ in range(len(x)):
        if x[_] == "B":
            strt = _
            break
    for _ in range(len(x)-1,-1,-1):
        if x[_] == "B":
            end = _
            break
    print(len(x[strt:end+1]))