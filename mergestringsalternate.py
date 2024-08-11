#https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_length = min(len(word1), len(word2))
        res = ""
        for w in range(min_length):
            res += word1[w]+word2[w]

        # Append the remaining part of the longer string (if any)
        res += word1[min_length:] + word2[min_length:]

        return res
        
