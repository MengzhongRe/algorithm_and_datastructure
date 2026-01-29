#
# @lc app=leetcode.cn id=300 lang=python
#
# [300] 最长递增子序列
#
# 贪心+二分查找算法
# 我们需要维护一个数组 tails（或者叫 d），其中 tails[i] 代表长度为 i+1 的所有上升子序列中，结尾最小的那个数。
# 为什么结尾越小越好？
# 因为结尾越小，后面接上一个更大的数的可能性就越大（门槛更低）。
# 算法流程
# 遍历 nums 中的每个数 num：
# 如果 num 比 tails 的最后一个元素还大：
# 说明可以直接接在最长序列后面，直接把 num 追加到 tails 末尾。
# 如果 num 小于或等于 tails 的最后一个元素：
# 我们需要在 tails 中找到第一个大于等于 num 的元素，并用 num 替换它。
# 这一步的意义：我们用一个更小的数替换了原来的结尾，虽然序列长度没变，但让这个序列的“增长潜力”变大了（变得更平缓了）。
# 查找过程是有序的，所以可以使用 二分查找。
# @lc code=start
import bisect

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        n = len(nums)

        tails = []

        for num in nums:
            if not tails or num > tails[-1]:
                tails.append(num)
            else:
                idx = bisect.bisect_left(tails,num)
                tails[idx] = num
        
        return len(tails)



# @lc code=end
#空间复杂度:O(N)
#时间复杂度:O(N^2)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        n = len(nums)
        # 用动态规划解的核心是定义dp数组，这里dp[i]定义为以nums[i]为结尾的nums的最长严格递增子序列的长度
        # 由于每个都可以取自身为严格递增子序列，因此全初始化为1
        dp = [1] * n
        # 遍历每一个nums[i],表示以nums[i]为结尾时，考虑前面可以＋哪些合法的序列
        for i in range(1,n):
            # 遍历i 之前的每一个j，看看是否nums[i] > nums[j]，也就是是否可以把nums[i] 加到以nums[j]为结尾的最长子序列的后面构成更长的子序列
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j] + 1)
                
        return max(dp)