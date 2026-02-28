class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if word.find(ch) == -1:
            return(word)
        else:
            return(word[word.index(ch)::-1] + word[(word.index(ch))+1:])
