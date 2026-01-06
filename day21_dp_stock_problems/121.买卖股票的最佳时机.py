#
# @lc app=leetcode.cn id=121 lang=python
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],-prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]+prices[i])
        
        return dp[-1][1]
        
# @lc code=end
#时间复杂度:O(N)
#空间复杂度:O(N)

#以下是滚动数组优化版本，实现空间复杂度为O(1)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        dp = [-prices[0],0]

        for i in range(1,len(prices)):
            new_hold = max(dp[0],-prices[i])

            new_not_hold = max(dp[1],dp[0]+prices[i])

            dp[0],dp[1] = new_hold,new_not_hold

        return dp[1]


