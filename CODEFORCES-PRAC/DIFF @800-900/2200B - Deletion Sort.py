t = int(input())
for _ in range(t):
    n = int(input())
    ele = list(map(int,input().split()))
    if ele == sorted(ele):
        print(len(ele))
    else:
        print(1)
