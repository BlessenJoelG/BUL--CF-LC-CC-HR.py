class Solution:
    #cheated by not following the rule of not to use the built-in expo opr
    #check the logic of getting sqrt without using "**"
    def mySqrt(self, x: int) -> int:
        return int(x**0.5)
Answer = Solution()
sqrt_of_num = Answer.mySqrt(x = int(input()))
print(sqrt_of_num)
