#
# @lc app=leetcode.cn id=494 lang=python
#
# [494] 目标和
#

# @lc code=start
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total_sum = sum(nums)
        if abs(target) > total_sum or (total_sum + target) % 2 != 0:
            return 0
        bag_size = (total_sum + target) // 2
        dp = [0] * (bag_size +1)
        dp[0] = 1

        for num in nums:
            for j in range(bag_size,num-1,-1):
                dp[j] += dp[j-num]

        return dp[bag_size]
# @lc code=end
#时间复杂度:O(N*bag_size)
#空间复杂度:O(bag_size)