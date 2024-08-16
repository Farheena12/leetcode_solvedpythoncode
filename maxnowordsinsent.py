#https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/submissions/1357400730/


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([len(s.split()) for s in sentences])
        
