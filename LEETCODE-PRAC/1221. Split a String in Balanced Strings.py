class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c_r,c_l,c_r_l = 0,0,0
        for _ in s:
            if c_r!=0 and c_l!=0 and c_r == c_l :
                c_r_l = c_r_l + 1
                c_r,c_l = 0,0
            if _ == "R":
                c_r = c_r + 1
            else:
                c_l = c_l + 1
        return(c_r_l + 1)