#
# @lc app=leetcode.cn id=1049 lang=python
#
# [1049] 最后一块石头的重量 II
#

# @lc code=start
class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        total_sum = sum(stones)
        target = total_sum // 2
        dp = [0] * (target + 1)

        for stone in stones:
            for j in range(target,stone - 1,-1):
                dp[j] = max(dp[j],dp[j-stone] + stone)
        
        return (total_sum - dp[target]) - dp[target]
        
# @lc code=end
#时间复杂度:O(N*target)
#空间复杂度:O(target)
