# Day 20: 动态规划 - 打家劫舍系列 (House Robber Series)

**日期**: 2026-01-05
**主题**: 线性DP、环形DP、树形DP
**标签**: #DynamicProgramming #TreeDP

## 📝 核心逻辑总结
打家劫舍系列的核心约束是 **“相邻不可兼得”**。
*   **线性数组**：当前状态依赖于前两个状态（滚动变量优化）。
*   **环形数组**：**破环成链**，分类讨论（去头 or 去尾）。
*   **二叉树**：**后序遍历**，自底向上汇报状态（偷/不偷）。

---

## 题目一：198. 打家劫舍 (House Robber)
**难度**: Medium
**场景**: 线性数组，相邻不能偷。

### 💡 解题思路
对于第 `i` 间房，只有两种选择：
1.  **偷**：那么第 `i-1` 间一定不能偷。总金额 = `nums[i] + dp[i-2]`。
2.  **不偷**：那么第 `i-1` 间随意（取之前的最大值）。总金额 = `dp[i-1]`。

### 🔢 状态转移方程
$$ dp[i] = \max(dp[i-1], \quad dp[i-2] + nums[i]) $$

### 💻 空间优化代码 ($O(1)$ 空间)
使用滚动变量 `prev2`, `prev1`, `curr` 代替数组。

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        
        # prev2: dp[i-2], prev1: dp[i-1]
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            curr = max(prev1, prev2 + nums[i])
            # 滚动更新
            prev2 = prev1
            prev1 = curr
            
        return prev1
```

---

## 题目二：213. 打家劫舍 II (House Robber II)
**难度**: Medium
**场景**: **环形**数组，首尾相邻。

### 💡 解题思路 (破环成链)
首尾相连意味着 **Index 0 和 Index N-1 不能同时偷**。我们将问题拆解为两个线性问题：
1.  **情况 A**：一定不偷最后一个房子 $\rightarrow$ 偷 `nums[0 : n-1]`。
2.  **情况 B**：一定不偷第一个房子 $\rightarrow$ 偷 `nums[1 : n]`。

**最终结果**：`max(rob_linear(情况A), rob_linear(情况B))`。

---

## 题目三：337. 打家劫舍 III (House Robber III)
**难度**: Medium
**场景**: **二叉树**结构，父子节点不能同时偷。

### 💡 解题思路 (树形 DP)
使用 **后序遍历 (Bottom-up)**。每个节点需要从左右子节点获取信息，然后决定自己的策略。
递归函数 `rob_tree(node)` 返回一个数组 `[val_rob, val_not_rob]`：
*   `res[0]`: 偷当前节点的最大值。
*   `res[1]`: 不偷当前节点的最大值。

### 🔢 状态转移
1.  **偷当前节点 (`root.val`)**：
    *   左右孩子**绝对不能偷**。
    *   `res[0] = root.val + left[1] + right[1]`
2.  **不偷当前节点**：
    *   左右孩子**偷不偷都行**，取各自的最大值。
    *   `res[1] = max(left[0], left[1]) + max(right[0], right[1])`

### 💻 关键代码
```python
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        res = self.rob_tree(root)
        return max(res[0], res[1])

    def rob_tree(self, node):
        if not node: return [0, 0]
        
        # 后序遍历
        left = self.rob_tree(node.left)
        right = self.rob_tree(node.right)
        
        # 1. 偷我 (孩子必须不偷)
        val_rob = node.val + left[1] + right[1]
        
        # 2. 不偷我 (孩子随意)
        val_not_rob = max(left) + max(right)
        
        return [val_rob, val_not_rob]
```

---

## 📊 复杂度分析总结

| 题目 | 时间复杂度 | 空间复杂度 | 备注 |
| :--- | :--- | :--- | :--- |
| **198. 线性** | $O(N)$ | $O(1)$ | 使用滚动变量优化 |
| **213. 环形** | $O(N)$ | $O(1)$ | 运行两次线性逻辑 |
| **337. 树形** | **$O(N)$** | **$O(H)$** | $H$ 为树高度，空间消耗来自递归栈 |

**树形 DP 复杂度证明**：
*   **时间**：每个节点只被访问一次，且处理逻辑（加法/比较）是常数时间 $O(1)$，总耗时 $O(N)$。
*   **空间**：没有显式申请数组，但递归调用栈的深度取决于树的高度。最好情况 $O(\log N)$，最坏情况（链表）$O(N)$。