#
# @lc app=leetcode.cn id=213 lang=python
#
# [213] 打家劫舍 II
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
        
        def rob_linear(arr):
            if not arr:
                return 0
            if len(arr) == 1:
                return arr[0]
            
            prev2 = arr[0]
            prev1 = max(arr[0],arr[1])

            for i in range(2,len(arr)):
                curr = max(prev1,prev2+arr[i])
                prev2 = prev1
                prev1 = curr
            return prev1

        result1 = rob_linear(nums[:-1])
        result2 = rob_linear(nums[1:])

        return max(result1,result2)
        
        
        
# @lc code=end
#时间复杂度: O(n)
#空间复杂度: O(1)

