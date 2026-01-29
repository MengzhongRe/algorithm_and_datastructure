import random
from typing import List

class Solution():
    def sortArray(self,nums: List[int]) -> List[int]:
        """
        主函数入口
        """
        self.quicksort(nums,0,len(nums)-1)
        return nums
    
    def quicksort(self,nums: List[int],start: int,end: int):
        #1.递归终止条件：区间内没有元素或者只有一个元素
        if start >= end:
            return
        
        #2.随机选择基准值并交换到头部，防止O(n**2)时间复杂度
        rand_idx = random.randint(start,end)
        nums[start],nums[rand_idx] = nums[rand_idx],nums[start]

        #3.基准值和左右指针初始化
        privot = nums[start]
        left = start
        right = end

        #4.Partition逻辑
        while left < right:
            #关键点：右指针先动，防止Privot值被错误调换
            while left < right and nums[right] >= privot:
                right -= 1
            
            while left < right and nums[left] <= privot:
                left += 1
            
            #左右指针各找到一个数，需要把它们调换
            nums[left],nums[right] = nums[right],nums[left]
        
        #当循环结束，left = right，由于右指针找的是比Privot小的值,此时nums[left] 一定小于等于privot
        #此时需要把privot和nums[left]对调
        nums[start],nums[left] = nums[left],nums[start]

        #5.left值已经处理完毕，下面对左右两部分各进行递归调用
        self.quicksort(nums,start,left-1)
        self.quicksort(nums,left+1,end)

