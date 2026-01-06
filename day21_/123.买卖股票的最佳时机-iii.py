#
# @lc app=leetcode.cn id=123 lang=python
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        n = len(prices)
        dp = [[0] * 5 for _ in range(n)]
        dp[0][0],dp[0][2],dp[0][4] = 0,0,0
        dp[0][1],dp[0][3] = -prices[0],-prices[0]

        for i in range(1,n):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
            dp[i][2] = max(dp[i-1][2],dp[i-1][1]+prices[i])
            dp[i][3] = max(dp[i-1][3],dp[i-1][2]-prices[i])
            dp[i][4] = max(dp[i-1][4],dp[i-1][3]+prices[i])
        return dp[-1][4]

        
# @lc code=end
#时间复杂度:O(N)
#空间复杂度:O(N)

#以下是滚动变量优化版本：O(1)
class Solution(object):
     def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        buy1 = -prices[0]
        shell1 = 0
        buy2 = -prices[0]
        shell2 = 0

        for price in prices:
            buy1 = max(buy1,-price)
            shell1 = max(shell1,buy1+price)
            buy2 = max(buy2,shell1-price)
            shell2 = max(shell2,buy2+price)
        return shell2


