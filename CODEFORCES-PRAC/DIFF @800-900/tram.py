max_passengers = 0
cur_passengers = 0
n = int(input())
for i in range(n):
    stop_i = list(map(int,input().split()))
    a_i = stop_i[0]
    b_i = stop_i[1]
    cur_passengers = (cur_passengers - a_i) + b_i
    if cur_passengers > max_passengers:
        max_passengers = cur_passengers
print(max_passengers)