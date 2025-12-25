#
# @lc app=leetcode.cn id=435 lang=python
#
# [435] 无重叠区间
#

# @lc code=start
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals: # 剪纸
            return 0
        
        counts = 0 # 计数
        intervals.sort(key=lambda x:x[1]) #先根据区间的右边界从小到大排序
        end = intervals[0][1] # 

        for i in range(1,len(intervals)):# 从第二个区间开始遍历
            if intervals[i][0] < end: # 如果新区见的左边界<旧的右边界那么抛弃它
                counts += 1 # 计数
            else:
                end = intervals[i][1] # 否则保留该区间并更新边界
        
        return counts
        
# @lc code=end
#时间复杂度：O(nlogn)主要受排序影响
#空间复杂度：O(1)/O(N)
