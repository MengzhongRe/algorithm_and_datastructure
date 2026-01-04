#
# @lc app=leetcode.cn id=139 lang=python
#
# [139] 单词拆分
#

# @lc code=start
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1,len(s) + 1):
            for word in wordDict:
                word_len = len(word)
                if i >= word_len and s[i-word_len:i] == word and dp[i-word_len]:
                    dp[i] = True
                    break
        return dp[len(s)]

        
# @lc code=end
#时间复杂度: O(n*m*l)
#空间复杂度: O(n)
#n为字符串s的长度，m为wordDict的长度，l为wordDict中单词的平均长度

