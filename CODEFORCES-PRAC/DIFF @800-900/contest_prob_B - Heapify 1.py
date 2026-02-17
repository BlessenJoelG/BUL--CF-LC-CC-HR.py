n_dis_int = []

t = int(input())
for _ in range(t):
    n = int(input())
    n_dis_int.extend(map(int,input().split()))
    check_sort = n_dis_int.sort()
    temp = n_dis_int[1]
    n_dis_int[1] = n_dis_int[3]
    n_dis_int[3] = temp
    if n_dis_int == check_sort:
        print("yes")
    else:
        print("no")