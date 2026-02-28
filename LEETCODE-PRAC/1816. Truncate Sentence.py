class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split(" ")
        del s[k:]
        s = " ".join(s)
        return(s)
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split(" ")
        return(" ".join(s[0:k]))