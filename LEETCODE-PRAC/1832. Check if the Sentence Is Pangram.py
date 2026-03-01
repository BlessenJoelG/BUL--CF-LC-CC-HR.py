class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence = {sentence[_] for _ in range(len(sentence))}
        if len(sentence) == 26:
            return True
        else:
            return False
