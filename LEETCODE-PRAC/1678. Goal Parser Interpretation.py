class Solution:
    def interpret(self, command: str) -> str:
        y = (command.replace("()","o"))
        z = (y.replace("(al)","al"))
        return z