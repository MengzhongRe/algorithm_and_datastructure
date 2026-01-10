#
# @lc app=leetcode.cn id=72 lang=python
#
# [72] 编辑距离
#

# @lc code=start
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m,n = len(word1),len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        for i in range(1,m + 1):
            for j in range(1,n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1],dp[i - 1][j],dp[i][j - 1]) + 1
        
        return dp[m][n]
   
# @lc code=end
#时间复杂度:O(M*N)
#空间复杂度:O(M*N)
#下面给出两行滚动变量优化版本
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) < len(word2):
            word1,word2 = word2,word1
        
        m,n = len(word1),len(word2)
        prev = list(range(n + 1))
        curr = [0] * (n + 1)
        for i in range(1,m + 1):
            curr[0] = i
            for j in range(1,n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = min(prev[j - 1],prev[j],curr[j - 1]) + 1
            prev = curr[:]
        
        return prev[n]

#一维数组+临时变量滚动优化：
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m,n = len(word1),len(word2)

        dp = list(range(n + 1))

        for i in range(1,m + 1):
            left_up = dp[0]
            dp[0] = i
            for j in range(1,n + 1):
                next_left_up = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = left_up
                else:
                    dp[j] = min(dp[j],left_up,dp[j - 1])
                
                left_up = next_left_up
        
        return dp[n]


