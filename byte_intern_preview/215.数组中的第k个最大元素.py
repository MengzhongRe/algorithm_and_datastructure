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
        min_heap = [] # 初始化一个空的最小堆，其中堆顶是堆中最小的元素

        for num in nums: # 遍历原数组
            if len(min_heap) < k: # 如果此时最小堆不到k个元素
                heapq.heappush(min_heap,num) # 将该元素推入堆中，会自动调整堆结构（时间复杂度O(logk）)
                # 使得堆顶的元素是其中最小的元素
            else: # 如果堆中已经有k个元素了
                if num > min_heap[0]: # 需要比较新元素与堆顶元素（也就是堆中的最小值），如果其比堆顶元素小
                    # 则说明其比堆中所有元素都小，直接跳过。但如果其比堆顶元素大，则把堆顶元素pop出来，然后把
                    # 新元素加入到堆中， 并自动调整堆结构
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