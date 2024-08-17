#https://leetcode.com/problems/removing-stars-from-a-string/submissions/1358837210/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def removeStars(self, s: str) -> str:
        stack =[]
        for char in s:
            if char == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        res= "".join(stack)
        return res

        
