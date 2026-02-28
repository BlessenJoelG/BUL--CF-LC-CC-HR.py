class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        sentence_len = []
        for i in sentences:
            x = i.split(" ")
            sentence_len.append(len(x))
        return(max(sentence_len))
Answer = Solution()
Answer.mostWordFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"])