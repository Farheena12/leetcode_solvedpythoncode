#https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/submissions/1357894437/

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        sum = 0
        for i,j in zip(seats,students):
            sum += abs(i-j)
        return sum
         
        
