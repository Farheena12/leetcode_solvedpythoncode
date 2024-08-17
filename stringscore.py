#https://leetcode.com/problems/score-of-a-string/submissions/1358646890/

class Solution:
    def scoreOfString(self, s: str) -> int:
        score = sum([abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s)-1)])
        return score
        
