#https://leetcode.com/problems/permutation-difference-between-two-strings/description/

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        return sum([abs(t.find(char) - idx_s) for idx_s, char in enumerate(s)])

        
