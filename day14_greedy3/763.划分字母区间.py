#
# @lc app=leetcode.cn id=763 lang=python
#
# [763] 划分字母区间
#

# @lc code=start
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last_index = {}
        for i, char in enumerate(s):
            last_index[char] = i
            
        result = []
        start = 0
        end = 0
        
        # 2. 再次遍历，找切分点
        for i, char in enumerate(s):
            # 贪心：当前片段的结束位置，至少要是当前字符的最后位置
            end = max(end, last_index[char])
            
            # 如果走到了这个片段的边界
            if i == end:
                result.append(end - start + 1)
                start = i + 1 # 更新下一个片段的起点
                
        return result
#时间复杂度:O(N)
#空间复杂度:O(1)哈希表最多存储26个字母
# @lc code=end

