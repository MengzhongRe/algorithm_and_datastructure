#
# @lc app=leetcode.cn id=45 lang=python
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        
        cur_cover = 0   #当前步的边界
        next_cover = 0  #下一步的边界
        steps = 0   #已经走过的步数

        for i in range(len(nums)-1):    #只需循环到列表的倒数第二个
            next_cover = max(next_cover,i + nums[i])

            if i == cur_cover:  #如果指针已经走到了当前步的边界
                steps += 1  #那么必须要走一步
                cur_cover = next_cover  #同时由于已经走了一步因此必须把当前覆盖范围更新为先前下一步的覆盖范围

            if cur_cover >= len(nums) - 1: #如果当前覆盖范围已经达到列表最后一个下标
                break   #结束循环

        return steps 

        
# @lc code=end
# 时间复杂度：O(N)
# 空间复杂度：O(1)

