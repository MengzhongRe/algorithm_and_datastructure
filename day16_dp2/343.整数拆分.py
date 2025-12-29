#
# @lc app=leetcode.cn id=343 lang=python
#
# [343] 整数拆分
#

# @lc code=start
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        """ dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3,n + 1):
            for j in range(1,i):
                dp[i] = max(dp[i],max(j * (i - j),j * dp[i - j]))
        return dp[n] """
    
        if n <= 3:
            return n - 1
        
        quotinent = n // 3
        remainder = n % 3

        if remainder == 0:
            return 3 ** quotinent
        elif remainder == 1:
            return 3 ** (quotinent - 1) * 4
        else:
            return 3 ** quotinent * 2
    
# @lc code=end
#时间复杂度：O(n^2)
#空间复杂度：O(n)
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n - 1
        quotinent = n // 3
        remainder = n % 3

        if remainder == 0:
            return 3 ** quotinent
        elif remainder == 1:
            return 3 ** (quotinent - 1) * 4
        else:
            return 3 ** quotinent * 2
#时间复杂度：O(1)
#空间复杂度：O(1)