A_sum,D_sum = 0,0
n = int(input())
s = input()
for x in range(n):
    if s[x] == "A":
        A_sum = A_sum + 1
    else:
        D_sum = D_sum + 1
if A_sum > D_sum:
    print("Anton")
elif A_sum == D_sum:
    print("Friendship")
else:
<<<<<<< HEAD
    print("Danik")
=======
    print("Danik")
>>>>>>> 781f09e5da9711298aa1fb35f8d4a8f516177b5c
