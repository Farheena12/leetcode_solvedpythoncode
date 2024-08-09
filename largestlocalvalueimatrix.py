#https://leetcode.com/problems/largest-local-values-in-a-matrix/

import numpy as np
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        grid = np.array(grid)
        n = grid.shape[0]

        l1 = []
        for i in range(n-2):
            l2 = []
            for j in range(n-2):
                l2.append(np.max((grid[i:i+3, j:j+3])))
            l1.append(l2)

        return l1

        
