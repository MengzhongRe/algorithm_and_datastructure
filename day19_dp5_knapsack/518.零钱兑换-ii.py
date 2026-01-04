#
# @lc app=leetcode.cn id=518 lang=python
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for j in range(coin,amount + 1):
                dp[j] += dp[j - coin]
        
        return dp[amount]
        
# @lc code=end
#时间复杂度：O(n*m)
#空间复杂度：O(m)
#n为coins的长度，m为amount的值
