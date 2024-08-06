#https://leetcode.com/problems/defanging-an-ip-address/description/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ""
        for i in address:
            if i ==".":
                res = res + "[.]"
            else:
                res = res + i
        return res  
        
