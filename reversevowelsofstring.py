#https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/1358773032/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = re.findall(r"[aeiouAEIOU]", s)
        return re.sub(r'[aeiouAEIOU]', lambda match: vowels.pop(), s)
