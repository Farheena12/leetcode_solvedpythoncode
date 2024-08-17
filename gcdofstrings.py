#https://leetcode.com/problems/greatest-common-divisor-of-strings/submissions/1358682506/?source=submission-noac

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        shorter, longer = (str1,str2) if len(str1) < len(str2) else (str2,str1)
        for i in range(len(shorter),0,-1):
            divi = shorter[:i]
            if len(str1) % len(divi) == 0 and len(str2) % len(divi) == 0:
                if divi * (len(str1) // len(divi)) == str1 and divi * (len(str2) //  len(divi))== str2 :
                    return divi
        return ""

        
