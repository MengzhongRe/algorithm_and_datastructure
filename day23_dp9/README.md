# Day 23: 动态规划 - 子序列问题 (Subsequence)

**日期**: 2026-01-07
**主题**: 子数组 vs 子序列、二维 DP 字符串匹配
**标签**: #DynamicProgramming #String

## 🧠 核心概念区分

在 DP 问题中，辨析 **连续性** 至关重要：

1.  **子序列 (Subsequence)**:
    *   **不要求连续**。例如 `[1, 3, 5]` 是 `[1, 2, 3, 4, 5]` 的子序列。
    *   **状态定义**：通常需要 $O(N^2)$ 或二维 DP，因为需要“回头看”之前的状态。
2.  **子数组/子串 (Subarray/Substring)**:
    *   **必须连续**。例如 `[1, 2]` 是，但 `[1, 3]` 不是。
    *   **状态定义**：通常只需要 $O(N)$，因为状态只能由 `i-1` 推导而来，一旦断开就重置。

---

## 题目一：300. 最长递增子序列 (LIS)
**难度**: Medium
**类型**: **子序列 (不连续)**

### 💡 核心思路
不能简单定义为“前 i 个元素的最长长度”，必须定义为 **“以 nums[i] 结尾”** 的最长长度。
这样才能保证递增关系的判断（只有知道结尾是谁，才能知道能不能接在后面）。

### 🔢 状态转移
1.  **定义**：`dp[i]` 表示若以 `nums[i]` 为结尾的`nums`的最长递增子序列的长度。
2.  **状态转移公式**：
    遍历 `i` 之前的所有 `j`，如果nums[i] > nums[j],那么就可以把nums[i] 加到已经算好的如果以nums[j]为结尾的最长严格递增子序列的后面，这样就可能构成更长的子序列：
    $$\text{if } nums[i] > nums[j]: \quad dp[i] = \max(dp[i], dp[j] + 1)$$
3.  **初始化**：`dp` 全为 1（每个元素自身就是长度 1）。
4.  **结果**：取dp数组所有元素的最大值：`max(dp)`。

### 💻 关键代码
```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
```
*(复杂度: Time $O(N^2)$, Space $O(N)$)*

### 贪心 + 二分查找
**时间复杂度为O(nlogn),空间复杂度为O(n)**

### 💡核心思路

我们需要维护一个数组 `tails`，其中 `tails[i]` 代表长度为 i+1 的所有严格上升子序列中，结尾最小的那个数。
为什么结尾越小越好？
因为结尾越小，后面接上一个更大的数的可能性就越大（门槛更低）。

遍历 `nums` 中的每个数 `num`：如果 `num` 比 `tails` 的最后一个元素还大：
说明可以直接接在最长子序列后面形成新的更长的严格递增子序列，直接把 num 追加到 tails 末尾。
如果 `num` 小于或等于 `tails` 的最后一个元素：
我们需要在 `tails` 中找到第一个大于等于 `num` 的元素，并用 `num` 替换它。
**这一步的意义：我们用一个更小的数替换了原来的结尾，虽然序列长度没变，但让这个序列的“增长潜力”变大了（变得更平缓了）。
查找过程是有序的，所以可以使用 二分查找**

### 💻 关键代码
标准二分查找代码(必背)*迭代版本*
```python
def binary_search(nums: List[int],target: int) -> int:
    if not nums:
        return -1

    n = len(nums)
    left,right = 0,n - 1
    while left <= right:
        mid = left + (right - left) // 2 # 防止整型溢出，python不会，但java，c是好的写法
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid +1
        else:
            right = mid - 1
    return -1
``` 

**手动编写二分查找**实现找到第一个大于等于`target`的`nums`数组的索引
```python
def binary_search_left(nums: List[int],target: int) -> int:
    left,right = 0,len(nums) # right初始化为len(nums),而不是len(nums)-1,是因为如果target比所有数都大，则函数需要返回len(nums),即数组最后一个下标+1，若right初始化为len(nums)-1,则永远不会返回len(nums)
    while left < right: # 左闭右开循区间，迭代终止条件为left == right,此时left和right就是返回值
        mid = left + (right - left) // 2
        if nums[mid] < target: # 若中间值小于taget，则由于我们要找的是比大于等于target的第一个值，所以一定在右边
            left = mid +1
        else: # 若中间值等于target,则说明目标值是mid,或mid左侧但不确定；若中间值大于target，则也说明目标值在包括mid的左侧，若依righr不能 - 1
            right = mid
    
    retun left
```
### 为什么以上二分查找第一个大于等于target的数字下表的代码不会出现死循环？一定成立？

### 🛡️ 第一道防线：向下取整的魔法 (`// 2`)

二分查找死循环的万恶之源，永远发生在区间只剩最后两个元素（即 `right - left == 1`）的时候。

请看你的 `mid` 计算公式：
`mid = left + (right - left) // 2`

因为 Python 的 `//` 是**向下取整（Floor Division）**，这就导致了一个绝对的数学定律：
**只要 `left < right`，计算出的 `mid` 永远严格小于 `right`！**

我们可以用极限情况（相邻的两个指针）来代入测试：
假设 `left = 0`，`right = 1`（区间里只有 1 个元素 `nums[0]`）：
* `mid = 0 + (1 - 0) // 2`
* `mid = 0 + 1 // 2`
* **`mid = 0`**

你看，当 `left` 和 `right` 紧挨着的时候，**`mid` 永远会偏向（等于）`left`，而绝对不可能等于 `right`！**

---

### 🗡️ 第二道防线：两个分支的绝对收缩

既然我们证明了 `left <= mid < right`，我们再来看你的两个 `if-else` 分支，看看区间是不是真的在缩小：

1. **分支 A：`left = mid + 1`**
   因为我们已知 `mid >= left`。
   那么新的 `left` = `mid + 1`，它绝对**严格大于**旧的 `left`。
   **结论：左边界向右推进，区间缩小！**

2. **分支 B：`right = mid` (你最担心的分支)**
   你担心 `right = mid` 会不会让 `right` 停在原地不动？
   绝对不会！因为我们刚才在第一道防线证明了：**`mid` 永远严格小于旧的 `right`（`mid < right`）**。
   那么当你执行 `right = mid` 时，新的 `right` 绝对**严格小于**旧的 `right`！
   **结论：右边界向左推进，区间缩小！**

既然不管是走 `if` 还是走 `else`，区间都在**严格缩小**，而且循环条件是 `while left < right`，那么它们总有一次会撞在一起变成 `left == right`，循环必定完美终止！

---

### 💣 真正的死循环陷阱在哪里？（反面教材）

为了让你彻底看透，我给你展示一个**真正会导致死循环的二分查找**（也就是我们在找“右边界”时极易犯的错）。

假设我们改一下需求，去找“最后一个小于等于 target 的数”。有的人会这么写：
```python
while left < right:
    mid = left + (right - left) // 2  # 还是向下取整
    if nums[mid] <= target:
        left = mid     # ❌ 灾难发生！
    else:
        right = mid - 1
```

**【死循环推演】**：
假设 `left = 0`, `right = 1`。
1. 计算 `mid = 0 + 1 // 2 = 0`。注意此时 **`mid == left`**！
2. 假设 `nums[0] <= target` 成立，走第一个分支：
3. **执行 `left = mid` $\rightarrow$ `left = 0`**。
4. **惨案发生**：旧的 `left` 是 0，新的 `left` 还是 0！区间完全没有收缩，下一轮继续算 `mid=0`，继续 `left=0`……**无限死循环！**

**【如何破解？】**
当你的逻辑要求你写下 `left = mid` 时，你必须配合**向上取整（Ceiling Division）**的 `mid` 计算公式：
`mid = left + (right - left + 1) // 2` 
加上这个 `+1` 之后，当 `left=0, right=1` 时，`mid` 就算出 `1`，它偏向了右边。此时再执行 `left = mid` (`left=1`)，区间就成功收缩了！

---

### 👑 终极总结论（背诵级口诀）

二分查找的边界收缩和死循环，可以用这两句绝密口诀彻底镇压：

1. **“求左边界（首选偏左的 mid）”**：
   使用 `mid = left + (right - left) // 2`（向下取整）。
   搭配 `left = mid + 1` 和 `right = mid`。**绝对安全，永不死循环！** （也就是你写的这段神仙代码）

2. **“求右边界（首选偏右的 mid）”**：
   使用 `mid = left + (right - left + 1) // 2`（向上取整）。
   搭配 `left = mid` 和 `right = mid - 1`。**绝对安全，永不死循环！**

**贪心+二分查找**（*用python内置函数bisect_left查找第一个大于等于num的小标*），
```python
import bisect
class Solution():
    def lengthOfLIS(self,nums: List[int]) -> int:
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
```

---

## 题目二：674. 最长连续递增序列
**难度**: Easy
**类型**: **子数组 (连续)**

### 💡 核心思路
因为要求 **连续**，`nums[i]` 只需要跟紧挨着的 `nums[i-1]` 比。不需要两层循环。

### 🔢 状态转移
1.  **递推**：
    *   如果 `nums[i] > nums[i-1]`：`dp[i] = dp[i-1] + 1`
    *   否则（断了）：`dp[i] = 1`
2.  **空间优化**：其实只需要一个变量记录当前连续长度即可，不需要数组。

---

## 题目三：1143. 最长公共子序列 (LCS)
**难度**: Medium
**类型**: **二维 DP** (两个字符串)

### 💡 核心思路
涉及两个字符串的子序列问题，标准解法是建立一个 **二维表格**。
行代表 `text1`，列代表 `text2`。

### 🔢 状态转移方程
**定义**：`dp[i][j]` 表示 `text1[0...i-1]` 和 `text2[0...j-1]` 的 LCS 长度。

**错位技巧**：DP 数组大小设为 `(L1+1) * (L2+1)`，其中 `dp[0][0]` 代表空串对比空串。这样可以避免处理 `i-1` 越界问题。

**递推逻辑**：
1.  **字符相等** (`text1[i-1] == text2[j-1]`)：
    *   这个字符一定在 LCS 里。
    *   继承左上角的结果 + 1。
    *   $$ dp[i][j] = dp[i-1][j-1] + 1 $$
2.  **字符不等**：
    *   继承左边或者上边的最大值（相当于删掉 text1 的当前字符，或者删掉 text2 的当前字符）。
    *   $$ dp[i][j] = \max(dp[i-1][j], \quad dp[i][j-1]) $$

### 💻 关键代码
```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 注意：dp索引是 i,j，对应字符串索引要减 1
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[m][n]
```

### 🚀 进阶：空间优化 (滚动数组)
由于 `dp[i]` 只依赖于 `dp[i-1]` (上一行)，我们可以只用两行数组滚动更新。
*   **Time**: $O(M \times N)$
*   **Space**: $O(\min(M, N))$

---

## 📊 总结图解

| 场景 | 状态定义 | 递推方向 | 复杂度 |
| :--- | :--- | :--- | :--- |
| **最长递增子序列** | 一维 `dp[i]` | 回头看 `0...i-1` | $O(N^2)$ |
| **最长连续递增** | 一维 `dp[i]` | 只看 `i-1` | $O(N)$ |
| **最长公共子序列** | 二维 `dp[i][j]` | 左上、左、上 | $O(N \times M)$ |
```