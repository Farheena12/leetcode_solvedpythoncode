#https://leetcode.com/problems/reverse-words-in-a-string/submissions/1358792163/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])
        
