#
# @lc app=leetcode.cn id=377 lang=python
#
# [377] 组合总和 Ⅳ
#

# @lc code=start
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1 )
        dp[0] = 1

        for i in range(1,target + 1):
                for num in nums:
                     if i >= num:
                        dp[i] += dp[i - num]
        
        return dp[target]
        
# @lc code=end
#时间复杂度: O(n*m)
#空间复杂度: O(m)
#n为target的值，m为nums的长度

