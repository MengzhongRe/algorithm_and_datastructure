#
# @lc app=leetcode.cn id=115 lang=python
#
# [115] 不同的子序列
#

# @lc code=start
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m,n = len(s),len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1
        
        for i in range(1,m + 1):
            for j in range(1,n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[m][n]


# @lc code=end

#时间复杂度:O(M*N)
#空间复杂度:O(M*N)

#两行滚动变量优化版本:O(min(M,N))
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m,n = len(s),len(t)
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)

        prev[0] = 1
        curr[0] = 1

        for i in range(1,m + 1):
            for j in range(1,n + 1):
                if s[i - 1] == t[j - 1]:
                    curr[j] = prev[j - 1] + prev[j]
                else:
                    curr[j] = prev[j]
            
            prev = curr[:]
        
        return prev[n]

#一行滚动优化版本：O(min(M,N))
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n = len(t)
        dp = [0] * (n + 1)
        dp[0] = 1

        for char_s in s:
            for j in range(n,0,-1):
                char_t = t[j - 1]
                if char_s == char_t:
                    dp[j] += dp[j - 1]
        
        return dp[n]
