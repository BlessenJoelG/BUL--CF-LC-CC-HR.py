class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        sentence_len = []
        for i in sentences:
            x = i.split(" ")
            sentence_len.append(len(x))
        return(max(sentence_len))