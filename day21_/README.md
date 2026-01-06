# Day 21: 动态规划 - 买卖股票系列 (Stock Trading Series)

**日期**: 2026-01-06
**主题**: 状态机 DP (State Machine)
**标签**: #DynamicProgramming #Array #Greedy

## 🧠 核心方法论：状态机模型

股票问题的本质不是预测未来，而是**状态转移**。
每一天，我们都处于某种“状态”（持有/不持有/卖出...）。今天的状态完全由**昨天**的状态推导而来。

**通用 DP 定义**：
*   `dp[0]` (Hold): 也就是持有股票，手里现金的最大值。
*   `dp[1]` (Not Hold): 也就是不持有股票，手里现金的最大值。

---

## 题目一：121. 买卖股票的最佳时机 (只能买卖一次)
**难度**: Easy
**关键限制**: 全程只能交易一次，意味着买入时，手里的本金一定是 **0**。

### 🔢 状态转移
1.  **持有 (Buy)**:
    *   延续昨天持有：`dp[0]`
    *   今天**第一次**买入：`0 - price` (注意：这里不是 `dp[1] - price`，因为买之前没赚过钱)
    *   $$ dp[0] = \max(dp[0], -prices[i]) $$
2.  **不持有 (Sell)**:
    *   延续昨天不持有：`dp[1]`
    *   今天卖出：`dp[0] + price`
    *   $$ dp[1] = \max(dp[1], dp[0] + prices[i]) $$

### 💻 关键代码
```python
# 初始化：dp[0] = -prices[0], dp[1] = 0
for price in prices:
    # 买入（只看成本，不看历史利润）
    dp[0] = max(dp[0], -price)
    # 卖出
    dp[1] = max(dp[1], dp[0] + price)
```

---

## 题目二：122. 买卖股票的最佳时机 II (无限次交易)
**难度**: Medium
**关键限制**: 可以多次买卖，意味着买入时，可以使用**之前赚的利润**。

### 🔢 状态转移
1.  **持有 (Buy)**:
    *   延续昨天持有：`dp[0]`
    *   今天买入（用赚的钱买）：`dp[1] - price` (**核心区别点**)
    *   $$ dp[0] = \max(dp[0], dp[1] - prices[i]) $$
2.  **不持有 (Sell)**:
    *   同上，没变化。
    *   $$ dp[1] = \max(dp[1], dp[0] + prices[i]) $$

### 💻 关键代码
```python
# 初始化：dp[0] = -prices[0], dp[1] = 0
for price in prices:
    # 买入（使用之前的利润）
    new_hold = max(dp[0], dp[1] - price)
    new_not_hold = max(dp[1], dp[0] + price)
    dp[0], dp[1] = new_hold, new_not_hold
```

---

## 题目三：123. 买卖股票的最佳时机 III (最多两次)
**难度**: Hard
**关键限制**: 最多 2 笔。单纯的 `Hold/Not Hold` 不够用了，必须区分是**第几次**交易。

### 🔢 五种状态定义
0.  **无操作**: 0
1.  **第一次持有 (Buy1)**: 第一次买入后的最大现金。
2.  **第一次卖出 (Sell1)**: 第一次卖出后的最大现金。
3.  **第二次持有 (Buy2)**: 第二次买入后的最大现金。
4.  **第二次卖出 (Sell2)**: 第二次卖出后的最大现金。

### 🔢 状态转移 (流水线)
*   `Buy1` 推导自 `初始状态`
*   `Sell1` 推导自 `Buy1`
*   `Buy2` 推导自 `Sell1` (用第一次赚的钱买第二次)
*   `Sell2` 推导自 `Buy2`

### 💻 关键代码
```python
# 初始化：只要涉及买入，初始资金就是 -price[0]
buy1 = -prices[0]
sell1 = 0
buy2 = -prices[0]
sell2 = 0

for price in prices:
    buy1 = max(buy1, -price)          # 第1次买
    sell1 = max(sell1, buy1 + price)  # 第1次卖
    
    buy2 = max(buy2, sell1 - price)   # 第2次买 (基于Sell1)
    sell2 = max(sell2, buy2 + price)  # 第2次卖
    
return sell2
```

---

## 📊 横向对比总结

| 题目 | 交易次数 | 买入状态转移方程 | 核心逻辑 |
| :--- | :--- | :--- | :--- |
| **121 (Easy)** | 1 次 | `max(hold, 0 - price)` | 本金永远是 0 |
| **122 (Med)** | 无限次 | `max(hold, not_hold - price)` | 本金是之前的累计利润 |
| **123 (Hard)** | 2 次 | `max(buy2, sell1 - price)` | 状态拆分，链式推导 |

### 🧠 复杂度分析
所有题目均可优化为：
*   **时间复杂度**: $O(N)$ (遍历一次数组)
*   **空间复杂度**: $O(1)$ (使用有限个变量滚动更新)