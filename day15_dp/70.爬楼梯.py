#
# @lc app=leetcode.cn id=70 lang=python
#
# [70] 爬楼梯
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n

        prev = 2
        curr = 3
        for i in range(4,n + 1):
            sum_val = prev + curr
            prev = curr
            curr = sum_val
        return sum_val 
        
# @lc code=end
#时间复杂度：O(N)
#空间复杂度：O(1)

