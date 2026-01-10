# Day 25: 动态规划 - 编辑距离与回文串 (Advanced String DP)

**日期**: 2026-01-11
**主题**: 编辑距离、区间 DP、中心扩展法
**标签**: #DynamicProgramming #String #Palindrome

## 📖 今日核心总结

今天攻克了 DP 中两个最特殊的板块：
1.  **编辑距离**：两个字符串之间“增删改”的最小代价。
2.  **回文问题**：**区间 DP** 的代表。
    *   核心难点在于**遍历顺序**：必须 **从下往上 (i 倒序)，从左往右 (j 正序)**。
    *   因为大区间 `[i, j]` 的状态依赖于内部小区间 `[i+1, j-1]`（即左下角）。

---

## 题目一：72. 编辑距离 (Edit Distance)
**难度**: Hard
**场景**: 将 `word1` 转换为 `word2` 的最少操作数（插入、删除、替换）。

### 💡 核心思路
**状态定义**：`dp[i][j]` 表示 `word1` 前 `i` 个字符转换成 `word2` 前 `j` 个字符的最小步数。

**递推公式**：
1.  **相等** (`w1[i-1] == w2[j-1]`)：
    *   不需操作，继承之前的代价。
    *   $$dp[i][j] = dp[i-1][j-1]$$
2.  **不等**：
    *   三路竞争，取最小 + 1。
    *   **删除** (删 w1): `dp[i-1][j]`
    *   **插入** (给 w1 插 / 删 w2): `dp[i][j-1]`
    *   **替换** (变身): `dp[i-1][j-1]`
    *   $$dp[i][j] = \min(\text{删}, \text{插}, \text{换}) + 1$$

### 💻 关键代码
```python
# 初始化：空串转换需要全删或全插
for i in range(m + 1): dp[i][0] = i
for j in range(n + 1): dp[0][j] = j

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
```

---

## 题目二：647. 回文子串 (Palindromic Substrings)
**难度**: Medium
**场景**: 统计字符串中有多少个连续回文子串。

### 方法 A：动态规划 (区间 DP)
*   **状态**：`dp[i][j]` (bool) 表示 `s[i...j]` 是否为回文。
*   **递推**：`if s[i] == s[j]`：
    *   `j - i <= 1` (如 "a", "aa") $\to$ True。
    *   `j - i > 1` (如 "aba") $\to$ 看内部 `dp[i+1][j-1]`。
*   **遍历顺序**：**i 从下往上，j 从左往右**。

```python
# DP 解法
for i in range(n - 1, -1, -1):
    for j in range(i, n):
        if s[i] == s[j]:
            # 这里的 <= 1 也可以放宽到 <= 2 (处理 "aba")
            if j - i <= 1 or dp[i+1][j-1]:
                dp[i][j] = True
                result += 1
```

### 方法 B：中心扩展法 (空间最优)
*   **思路**：回文一定有个中心。遍历每个中心，向两边扩散。
*   **中心点**：共有 $2N-1$ 个中心（$N$ 个单字符 + $N-1$ 个双字符间隙）。
*   **复杂度**：Time $O(N^2)$, **Space $O(1)$**。

```python
# 中心扩展法 (推荐)
def extend(s, left, right):
    count = 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        count += 1
        left -= 1
        right += 1
    return count

for i in range(n):
    res += extend(s, i, i)     # 奇数长度
    res += extend(s, i, i+1)   # 偶数长度
```
---

## 📊 总结对比

| 题目 | 类型 | 连续性 | 核心递推 | 遍历方向 |
| :--- | :--- | :--- | :--- | :--- |
| **编辑距离** | 双串 DP | / | `min(增,删,改)+1` | 正序 (1->N) |
| **回文子串** | 区间 DP | **连续** | `dp[i+1][j-1]` | **i 倒序, j 正序** |

*注：对于回文子串，中心扩展法通常优于 DP，因为空间复杂度为 $O(1)$。*