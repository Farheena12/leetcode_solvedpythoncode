#https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1_tot = []
        w2_tot = []
        w1_tot = "".join(word1)
        w2_tot = "".join(word2)
        if w1_tot == w2_tot:
            return True
        else:
            return False 

        
