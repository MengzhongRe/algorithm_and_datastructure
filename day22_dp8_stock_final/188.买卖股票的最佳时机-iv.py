#
# @lc app=leetcode.cn id=188 lang=python
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if not prices or k == 0:
            return 0
        dp = [[0] * (2 * k + 1) for _ in range(n)]
        #dp数组初始化，i为偶数dp[0][i] = 0,i为奇数dp[0][i] = -prices[0]
        for i in range(1,2 * k + 1,2):
            dp[0][i] = -prices[0]
        
        for i in range(1,n):
            dp[i][0] = 0
            for j in range(1,2 * k + 1):
                if j % 2 == 0:
                    dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]+prices[i])
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]-prices[i])

        return dp[-1][-1]
            
# @lc code=end
#时间复杂度:O(nk)
#空间复杂度:O(nk)

#下面给出滚动数组优化版本：
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or k == 0:
            return 0
        n = len(prices)

        dp = [0] * (2 * k + 1)
        for i in range(1,2 * k + 1,2):
            dp[i] = -prices[0]

        for price in prices:
            for j in range(0,2 * k -1,2):
                dp[j + 1] = max(dp[j+1],dp[j]-price)
                dp[j + 2] = max(dp[j+2],dp[j+1]+price)
        return dp[-1]
#时间复杂度:O(nk)
#空间复杂度:O(k)




