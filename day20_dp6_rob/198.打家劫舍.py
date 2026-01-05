#
# @lc app=leetcode.cn id=198 lang=python
#
# [198] 打家劫舍
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]
# @lc code=end
#时间复杂度: O(n)
#空间复杂度: O(n)

#以下为空间复杂度为O(1)的滚动变量优化版
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        prev2 = nums[0]
        prev1 = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            curr = max(prev1,prev2+nums[i])
            prev2 = prev1
            prev1 = curr
        return prev1
