#https://leetcode.com/problems/smallest-even-multiple/submissions/1349982867/

#Approach 1
# class Solution:
#     def smallestEvenMultiple(self, n: int) -> int:
#         if n%2 ==0:
#             return n
#         else:
#             return (2*n)

#Approach 2
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n%2 ==0 else (2*n)
        

