#
# @lc app=leetcode.cn id=714 lang=python
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # if not prices:
        #     return 0
        
        # n = len(prices)
        # dp = [[0] * 2 for _ in range(n)]
        # dp[0][0] = -prices[0]

        # for i in range(1,n):
        #     dp[i][0] = max(dp[i-1][0],dp[i-1][1]-prices[i])
        #     dp[i][1] = max(dp[i-1][1],dp[i-1][0]+prices[i]-fee)

        # return dp[-1][-1] 
        if not prices:
            return 0
        
        hold = -prices[0]
        not_hold = 0

        for price in prices:
            hold = max(hold,not_hold - price)
            not_hold = max(not_hold,hold + price - fee)
        
        return not_hold
        
# @lc code=end
#时间复杂度:O(N)
#空间复杂度:O(N)

#下面给出滚动数组优化版本：O(1)
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0
        
        hold = -prices[0]
        not_hold = 0

        for price in prices:
            hold = max(hold,not_hold - price)
            not_hold = max(not_hold,hold + price - fee)
        
        return not_hold
#时间复杂度:O(N)
#空间复杂度:O(1)