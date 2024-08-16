#https://leetcode.com/problems/detect-capital/

import re

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        pattern = r'^[A-Z]+$|^[a-z]+$|^[A-Z][a-z]+$'
        return bool(re.match(pattern,word))
        
