s = "RLRRRLLRLL"
c_r = 0
c_l = 0
c_r_l = 0
for _ in s:
    if c_r!=0 and c_l!=0 and c_r == c_l :
        c_r_l = c_r_l + 1
        c_r,c_l = 0,0
    if _ == "R":
        c_r = c_r + 1
    else:
        c_l = c_l + 1
print(c_r_l+1)