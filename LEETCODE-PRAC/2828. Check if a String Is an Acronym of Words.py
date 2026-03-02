class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acro = ""
        for _ in words:
            acro = acro + _[0]
        if acro == s:
            return True
        else:
            return False
