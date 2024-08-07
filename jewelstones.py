https://leetcode.com/problems/jewels-and-stones/description/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for ele_j in (jewels):
            count = count+stones.count(ele_j)

        return count
        
