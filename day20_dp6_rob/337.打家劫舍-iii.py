#
# @lc app=leetcode.cn id=337 lang=python
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        result = self.rob_tree(root)
        return max(result[0],result[1])
    

    def rob_tree(self,node):
        if not node:
            return [0,0]
        
        left = self.rob_tree(node.left)
        right = self.rob_tree(node.right)

        val_rob = node.val + left[1] + right[1]
        val_not_rob = max(left[0],left[1]) + max(right[0],right[1])

        return [val_rob,val_not_rob]
        
# @lc code=end
#时间复杂度:O(N)
#空间复杂度:O(H)

