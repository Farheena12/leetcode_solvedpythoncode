#https://leetcode.com/problems/defanging-an-ip-address/description/

#Method 1: Using if and for loop
# class Solution:
#     def defangIPaddr(self, address: str) -> str:
#         res = ""
#         for i in address:
#             if i ==".":
#                 res = res + "[.]"
#             else:
#                 res = res + i
#         return res  

Method 2: Using replace method.
class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = address.replace('.', "[.]")
        return address  
        
        
