#
# @lc app=leetcode.cn id=416 lang=python
#
# [416] 分割等和子集
#

# @lc code=start
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = [0] * (target + 1)
        for num in nums:
            for j in range(target,num - 1,-1):
                dp[j] = max(dp[j],dp[j-num]+num)
            if dp[target] == target:
                return True
        return dp[target] == target
        
# @lc code=end
# 时间复杂度:O(n*m),伪多项式时间
#空间复杂度:O(n)
