#
# @lc app=leetcode.cn id=704 lang=python
#
# [704] 二分查找
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left,right = 0,len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
#时间复杂度:O(log N),空间复杂度:O(N)  
# @lc code=end
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.search_baniary(0,len(nums)-1,nums,target)

    
    def search_baniary(self,left,right,nums,target):
        if left > right:
            return -1
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.search_baniary(mid+1,right,nums,target)
        else:
            return self.search_baniary(left,mid-1,nums,target)
#递归版本空间复杂度为:O(log N)不推荐