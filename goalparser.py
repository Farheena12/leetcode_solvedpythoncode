#https://leetcode.com/problems/goal-parser-interpretation/submissions/1357872787/

class Solution:
    def interpret(self, command: str) -> str:
        com= command.replace("()","o")
        command =com.replace("(al)","al")
        return command
        
