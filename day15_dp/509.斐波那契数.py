#
# @lc app=leetcode.cn id=509 lang=python
#
# [509] 斐波那契数
#

# @lc code=start
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        
        prev = 0
        curr = 1

        for i in range(2,n + 1):
            sum_val = prev + curr
            prev = curr
            curr = sum_val
        
        return sum_val

        


        
# @lc code=end
#时间复杂度：O(N)
#空间复杂度：O(1)

