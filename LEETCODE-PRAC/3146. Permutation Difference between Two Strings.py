class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        c = 0
        for _ in s:
            c = c + abs(s.index(_) - t.index(_))
        return(c)