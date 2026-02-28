class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split(" ")
        del s[k:]
        s = " ".join(s)
        return(s)