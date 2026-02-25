class Solution:
    def convertDateToBinary(self, date: str) -> str:
        x = date.split("-")
        c = ""
        for _ in x:
            c = c + bin(int(_))[2:] + "-"
        date = str(c).rstrip("-")
        return(date)