class Solution:
    def maxDistinct(self, s: str) -> int:
        num_of_s = {_ for _ in s}
        return(len(num_of_s))