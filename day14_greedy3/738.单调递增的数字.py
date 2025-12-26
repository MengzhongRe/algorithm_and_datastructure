#
# @lc app=leetcode.cn id=738 lang=python
#
# [738] 单调递增的数字
#

# @lc code=start
class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = list(str(n))
        flag = len(s)

        for i in range(len(s)-1,0,-1):
            if s[i-1] > s[i]:
                s[i-1] = str(int(s[i-1]) - 1)
                flag = i
        
        for i in range(flag,len(s)):
            s[i] = '9'
        
        return int("".join(s))
时间复杂度:O(N)
空间复杂度:O(N)
# @lc code=end

