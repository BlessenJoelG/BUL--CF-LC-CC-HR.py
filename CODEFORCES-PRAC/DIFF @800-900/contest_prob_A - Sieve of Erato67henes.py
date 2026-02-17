t,n_pos_int = int(input()),[]
for _ in range(t):
    n = int(input())
    n_pos_int.extend(map(int,input().split()))
    if 1 and 67 in n_pos_int:
        print("yes")
    else:
        print("no")
    n_pos_int.clear()