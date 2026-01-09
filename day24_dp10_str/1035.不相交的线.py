#
# @lc app=leetcode.cn id=1035 lang=python
#
# [1035] 不相交的线
#

# @lc code=start
class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        if len(nums1) < len(nums2):
            nums1,nums2 = nums2,nums1
        
        m,n = len(nums1),len(nums2)
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)

        for i in range(1,m + 1):
            for j in range(1,n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(prev[j],curr[j - 1])
            
            prev = curr[:]
        
        return prev[n]
# @lc code=end
#时间复杂度:O(M*N)
#空间复杂度:O(min(M,N))
