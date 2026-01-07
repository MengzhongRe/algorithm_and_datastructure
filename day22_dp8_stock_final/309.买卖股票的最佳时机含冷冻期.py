#
# @lc app=leetcode.cn id=309 lang=python
#
# [309] 买卖股票的最佳时机含冷冻期
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
        
        hold = -prices[0]
        sold = 0 
        rest = 0

        for price in prices:
            prev_hold,prev_sold,prev_rest = hold,sold,rest

            hold = max(prev_hold,prev_rest-price)
            sold = prev_hold+price
            rest = max(prev_rest,prev_sold)
        return max(sold,rest)
        
# @lc code=end
#时间复杂度:O(N)
#空间复杂度:O(1)
