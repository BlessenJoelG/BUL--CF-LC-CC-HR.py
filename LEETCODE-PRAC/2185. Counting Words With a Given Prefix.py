class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for _ in words:
            if _.startswith(pref):
                count = count + 1
        return(count)
