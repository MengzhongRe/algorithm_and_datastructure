#
# @lc app=leetcode.cn id=1143 lang=python
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        len1,len2 = len(text1),len(text2)
        dp = [[0] * (len2+1) for _ in range(len1 +1)]

        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        return dp[len1][len2]
        
# @lc code=end
#时间复杂度:O(M*N)
#空间复杂度:O(M*N)

#滚动变量优化版本:O(min(M,N))
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # 优化：确保 text2 是短的那个，用来开数组，节省空间
        if len(text1) < len(text2):
            text1,text2 = text2,text1
        
        m,n = len(text1),len(text2)
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)

        for i in range(1,m + 1):
            for j in range(1,n + 1):
                if text1[i-1] == text2[j - 1]:
                    curr[j] = prev[j-1] + 1
                else:
                    curr[j] = max(prev[j],curr[j-1])

            prev = curr[:]
        return prev[n]

