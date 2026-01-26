#
# @lc app=leetcode.cn id=215 lang=python
#
# [215] 数组中的第K个最大元素
#
#最小堆解决该问题，空间复杂度:O(K),时间复杂度:O(N*logK)
# @lc code=start
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap,num)
            else:
                if num > min_heap[0]:
                    heapq.heapreplace(min_heap,num)

        return min_heap[0]

# @lc code=end
#用快速选择方法有一个具有多个重复数值的测试用例会超时
import random

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        #转换目标索引
        target_index = n - k

        left = 0
        right = n - 1

        while True:
            #执行分区
            privot_index = self.partition(nums,left,right)
            #判断privot_index和target_index的关系
            if privot_index == target_index:
                return nums[privot_index]
            elif privot_index < target_index:
                left = privot_index + 1
            else:
                right = privot_index - 1
                
    
    
    def partition(self,nums,start,end):
        #1.随机化选择基准并交换头部，避免O(N**2)时间复杂度
        rand_idx = random.randint(start,end)
        nums[start],nums[rand_idx] = nums[rand_idx],nums[start]

        #2.初始化基准值和左右指针
        privot = nums[start]
        left = start
        right = end

        #3.prtition逻辑
        while left < right:
            #关键点：先让右指针先动，防止privot被错误调换
            while left < right and nums[right] >= privot:
                right -= 1
            while left < right and nums[left] <= privot:
                left += 1
            
            #左右指针都已经找到一个值，调换
            nums[left],nums[right] = nums[right],nums[left]
        
        #4.当循环结束时，left == right,此时由于右指针找的是比Privot小的数所以nums[left]<= privot
        nums[start],nums[left] = nums[left],nums[start]
        #5.返回privot的索引值
        return left