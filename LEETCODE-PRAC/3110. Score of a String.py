class Solution:
    def scoreOfString(self, s: str) -> int:
        c = 0
        s_ascii = [ord(_) for _ in s]
        for _ in range(0,len(s_ascii)-1):
             c = c + abs(s_ascii[_]-s_ascii[_+1])
        return c