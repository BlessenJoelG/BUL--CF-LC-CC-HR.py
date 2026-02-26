t = int(input())
for idx in range(t):
    x,c = input(),""
    y = ["q" if x[_] == "p" else "p" if x[_] == "q" else "w" for _ in range(len(x))]
    for i in y:
        c = c + i
    print(c[::-1])