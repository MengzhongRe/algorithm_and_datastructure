#
# @lc app=leetcode.cn id=647 lang=python
#
# [647] 回文子串
#

# @lc code=start
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        result = 0

        for i in range(n - 1,-1,-1):
            for j in range(i,n,1):
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                        result += 1
                    elif dp[i + 1][j - 1]:
                        dp[i][j] = True
                        result += 1
        
        return result

# @lc code=end
#时间复杂度:O(N^2)
#空间复杂度:O(N^2)
#下面给出中心扩展法空间复杂度为O(1)
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        n = len(s)

        for i in range(n):
            count += self.extend(s,i,i,n)
            count += self.extend(s,i,i+1,n)
        
        return count
    
    def extend(self,s,left,right,n):
        res = 0
        while left >= 0 and right < n and s[left] == s[right]:
            res += 1
            left -= 1
            right += 1
        return res