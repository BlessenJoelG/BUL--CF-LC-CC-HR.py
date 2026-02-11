# 4
# 27
# 99
# 123456
# 987654321
j = []
def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
t = int(input())
for _ in range(t):
    x = int(input())
    count = 0
    for y in range(x, x + 91): 
        if y - digit_sum(y) == x:
            count += 1
    j.append(count)
for _ in range(len(j)):
    print(j[_])    