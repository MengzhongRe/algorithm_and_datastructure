#
# @lc app=leetcode.cn id=674 lang=python
#
# [674] 最长连续递增序列
#

# @lc code=start
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        n = len(nums)
        result = 1
        dp = [1] * n

        for i in range(1,n):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
            
            if dp[i] > result:
                result = dp[i]
        
        return result
        
# @lc code=end
#时间复杂度：O(N)
#空间复杂度：O(N)
