#
# @lc app=leetcode.cn id=300 lang=python
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n
        result = 1

        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
            
            if dp[i] > result:
                result = dp[i]
        
        return result
    
        
# @lc code=end
#空间复杂度:O(N)
#时间复杂度:O(N^2)

