#
# @lc app=leetcode.cn id=1470 lang=python
#
# [1470] 重新排列数组
#

# @lc code=start
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        answer = []
        for i in range(n):
            answer += [nums[i],nums[i + n]]
        return answer

        
# @lc code=end

