#
# @lc app=leetcode.cn id=474 lang=python
#
# [474] 一和零
#

# @lc code=start
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in range(m+1)]
        for s in strs:
            zeroNum = s.count('0')
            oneNum = s.count('1')
            for j in range(n,oneNum-1,-1):
                for i in range(m,zeroNum-1,-1):
                    dp[i][j] = max(dp[i][j],dp[i-zeroNum][j-oneNum] +1)
        return dp[m][n]

        
# @lc code=end
#时间复杂度:O(L*m*n) L为strs的长度
#空间复杂度:O(m*n)

