class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = 0
        chk,pattern = [jewels[_]for _ in range(len(jewels))],[stones[x]for x in range(len(stones))]
        for _ in chk:
            c = c + pattern.count(_)
        return(c)