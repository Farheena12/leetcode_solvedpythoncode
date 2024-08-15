#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/submissions/1356631083/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [candy + extraCandies >= max(candies) for candy in candies]

        
