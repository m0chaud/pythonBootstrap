class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richestCustomerWealth = 0
        for account in accounts:
            customerBalance = 0
            for balance in account:
                customerBalance = customerBalance + balance
            
            if customerBalance > richestCustomerWealth:
                richestCustomerWealth = customerBalance
        
        return richestCustomerWealth


        