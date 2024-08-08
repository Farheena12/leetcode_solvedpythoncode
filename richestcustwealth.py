#https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth_customers = []
        for account in accounts:
            wealth_customers.append(sum(account))

        return max(wealth_customers)
