#
# @lc app=leetcode.cn id=56 lang=python
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        
        # 1. 核心：按左边界排序
        intervals.sort(key=lambda x: x[0])
        
        # 把第一个放入结果集作为基准
        result = [intervals[0]]
        
        for i in range(1, len(intervals)):
            current = intervals[i]
            last_merged = result[-1]
            
            # 2. 检查是否重叠
            if current[0] <= last_merged[1]:
                # 3. 合并：右边界取最大值
                # 注意：左边界不需要动，因为排序保证了 last 的左边界一定更小
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # 不重叠，直接加入
                result.append(current)
                
        return result
时间复杂度：O(NlogN)
空间复杂度：O(N)或O(1)（取决于排序算法是否原地排序）


        
# @lc code=end

