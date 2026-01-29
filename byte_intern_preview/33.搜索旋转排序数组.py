#
# @lc app=leetcode.cn id=33 lang=python
#
# [33] 搜索旋转排序数组
#
# 时间复杂度:O(logN)符合二分查找，空间复杂度O（1）
# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums:
            return -1
        
        n = len(nums)
        left,right = 0,n -1
        
        while left <= right:
            mid = left + (right - left) // 2

            #若nums[mid] == target直接返回mid
            if nums[mid] == target:
                return mid
            
            # 若左区间是有序
            if nums[left] <= nums[mid]:
                # 则先判断target是否在该区间范围内
                if nums[left] <= target < nums[mid]:
                    right = mid - 1 # 则在左区间查找
                else:
                    left = mid + 1 # 否则就只能在右区间内查找
            else:# 若左区间无序则右区间一定有序,此时判断target是否在右区间范围内
                if nums[mid] < target <= nums[right]:
                    left = mid + 1 # 若在则查找右区间
                else:
                    right = mid - 1 # 否则查找左区间
        
        return -1
        
# @lc code=end

