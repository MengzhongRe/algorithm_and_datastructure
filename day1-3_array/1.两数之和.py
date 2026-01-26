#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#
#考察双指针,简单解法时间复杂度为:O(N^2),空间复杂度为O(1)
# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    return [i,j]
# @lc code=end

