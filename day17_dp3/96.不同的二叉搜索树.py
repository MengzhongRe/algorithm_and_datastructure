#
# @lc app=leetcode.cn id=96 lang=python
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        dp = [0] * (n + 1)
        dp[0],dp[1] = 1,1
        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]
        
# @lc code=end
#时间复杂度:O(N^2)
#空间复杂度:O(N)

