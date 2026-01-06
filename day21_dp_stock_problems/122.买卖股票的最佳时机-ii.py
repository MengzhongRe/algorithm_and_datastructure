#
# @lc app=leetcode.cn id=122 lang=python
#
# [122] 买卖股票的最佳时机 II
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
        
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]+prices[i])
        return dp[-1][1]
 
        
# @lc code=end
#时间复杂度:O(N)
#空间复杂度:O(N)

#以下同样给出滚动数组优化版：O(1)
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
            new_hold = max(dp[0],dp[1]-prices[i])

            new_not_hold= max(dp[1],dp[0]+prices[i])

            dp[0],dp[1] = new_hold,new_not_hold
        return dp[1]



