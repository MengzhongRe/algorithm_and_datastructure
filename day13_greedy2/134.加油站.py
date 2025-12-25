#
# @lc app=leetcode.cn id=134 lang=python
#
# [134] 加油站
#

# @lc code=start
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        curr_tank = 0

        for i in range(len(gas)):
            curr_tank += gas[i] - cost[i]

            if curr_tank < 0:
                start = i + 1
                curr_tank = 0
        return start
        
# @lc code=end
# 时间复杂度：O(N)
# 空间复杂度: O(1)
