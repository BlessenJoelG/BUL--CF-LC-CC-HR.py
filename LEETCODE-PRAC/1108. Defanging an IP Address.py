class Solution:
    def defangIPaddr(self, address: str) -> str:
        y = address.replace(".","[.]")
        return y