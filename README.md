# 🚀 LeetCode Journal & Algorithm Notes

[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![LeetCode](https://img.shields.io/badge/LeetCode-Daily-orange?style=flat&logo=leetcode&logoColor=white)](https://leetcode.cn/u/xiang-nan-zhao-bei-b/)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success)]()

> **"Algorithm is the art of efficiency."**

本仓库用于系统性记录我的算法学习之路。不仅仅是 AC 的代码堆砌，更包含了**解题思路的推导**、**数学证明**以及**通用算法模板**的提炼。

## 📖 核心目标 (Goals)

- **工程化 (Engineering)**: 所有代码均包含详细注释，遵循 PEP8 规范，具备可读性与可复用性。
- **体系化 (Systematic)**: 从线性的数组链表到非线性的树与图，再到动态规划与贪心，构建完整的知识图谱。
- **深度化 (In-depth)**: 拒绝死记硬背，通过 `README.md` 复盘每道题的**时间复杂度**与**空间复杂度**，探究最优解。

## 📂 项目结构 (Structure)

```text
.
├── 📂 day01_array/            # 按天/专题组织的训练单元
│   ├── solution.py            # Python 题解源码 (Type Hinted)
│   └── README.md              # 📝 核心：解题思路、图解与复杂度分析
├── 📂 day23_subsequence/
│   ├── ...
├── 📂 notes/                  # 🧠 核心资产：通用算法模板
│   ├── dp_knapsack_template.md
│   ├── backtracking_template.md
│   └── binary_tree_patterns.md
└── README.md                  # 项目主页
```

## 🗓️ 刷题进度 (Progress)

### Phase 1: 基础数据结构与算法

| Day | Topic (专题) | Problems (题目) | Diff | Solution & Notes | Key Takeaways (核心考点) |
|:---:|:---|:---|:---:|:---:|:---|
| **01** | Array & Hash | 1. Two Sum<br>27. Remove Element | 🟢 | [Link](./day01/README.md) | 哈希表空间换时间 |
| **04** | Linked List | 206. Reverse Linked List<br>141. Linked List Cycle | 🟢 | [Link](./day04/README.md) | 双指针迭代 / 递归 |
| **05** | Linked List+ | 21. Merge Two Sorted Lists<br>19. Remove Nth Node From End<br>20. Valid Parentheses | 🟢<br>🟡 | [Link](./day05/README.md) | 虚拟头节点 / 栈的应用 |
| **07** | Stack & Queue | 232. Implement Queue using Stacks<br>225. Implement Stack using Queues<br>239. Sliding Window Maximum | 🟢<br>🔴 | [Link](./day07/README.md) | **单调队列**处理滑动窗口 |
| **08** | Binary Tree | 104. Max Depth of Binary Tree<br>226. Invert Binary Tree<br>101. Symmetric Tree | 🟢 | [Link](./day08/README.md) | 递归思维 (DFS) |
| **09** | Tree Advanced | 102. Level Order Traversal<br>98. Validate BST<br>236. Lowest Common Ancestor | 🟡 | [Link](./day09/README.md) | BFS 层序遍历 / LCA 后序遍历 |

### Phase 2: 搜索与贪心

| Day | Topic (专题) | Problems (题目) | Diff | Solution & Notes | Key Takeaways (核心考点) |
|:---:|:---|:---|:---:|:---:|:---|
| **10** | Backtracking | 77. Combinations<br>46. Permutations<br>17. Letter Combinations | 🟡 | [Link](./day10/README.md) | 回溯模板：递归+撤销 |
| **11** | Backtracking+ | 78. Subsets<br>90. Subsets II<br>51. N-Queens | 🟡<br>🔴 | [Link](./day11/README.md) | 去重逻辑 / 棋盘问题 |
| **12** | Greedy Basics | 455. Assign Cookies<br>122. Best Time to Buy Stock II<br>55. Jump Game | 🟢<br>🟡 | [Link](./day12/README.md) | 局部最优推全局最优 |
| **13** | Greedy Mid | 45. Jump Game II<br>134. Gas Station<br>435. Non-overlapping Intervals | 🟡 | [Link](./day13/README.md) | 覆盖范围 / 区间调度排序 |
| **14** | Greedy Adv | 56. Merge Intervals<br>763. Partition Labels<br>738. Monotone Increasing Digits | 🟡 | [Link](./day14/README.md) | 区间合并 / 逆序贪心 |

### Phase 3: 动态规划 (Dynamic Programming)

| Day | Topic (专题) | Problems (题目) | Diff | Solution & Notes | Key Takeaways (核心考点) |
|:---:|:---|:---|:---:|:---:|:---|
| **15** | DP Basics | 509. Fibonacci Number<br>70. Climbing Stairs<br>746. Min Cost Climbing Stairs | 🟢 | [Link](./day15/README.md) | DP 五部曲 / 滚动数组优化 |
| **16** | 0-1 Knapsack | 0-1 Knapsack Theory<br>416. Partition Equal Subset Sum | 🟡 | [Link](./day16/README.md) | **倒序遍历** / 滚动数组 |
| **17** | Knapsack Vars | 1049. Last Stone Weight II<br>494. Target Sum<br>474. Ones and Zeroes | 🟡 | [Link](./day17_dp3/README.md) | 求组合数公式 / 二维费用背包 |
| **18** | Complete Pack | 322. Coin Change<br>279. Perfect Squares | 🟡 | [Link](./day18_dp4/README.md) | **正序遍历** / 凑满问题 |
| **19** | Pack Order | 518. Coin Change II<br>377. Combination Sum IV<br>139. Word Break | 🟡 | [Link](./day19_dp5_knapsack/README.md) | **组合(先物后包) vs 排列(先包后物)** |
| **20** | House Robber | 198. House Robber<br>213. House Robber II<br>337. House Robber III | 🟡 | [Link](./day20_dp6_rob/README.md) | 环形DP / 树形DP (后序) |
| **21** | Stock Series | 121. Stock I (One Transaction)<br>122. Stock II (Unlimited)<br>123. Stock III (2 Transactions) | 🟢<br>🔴 | [Link](./day21_dp_stock_problems/README.md) | 状态机 DP / 状态拆分 |
| **22** | Stock Adv | 188. Stock IV (k Transactions)<br>309. Stock with Cooldown<br>714. Stock with Transaction Fee | 🔴<br>🟡 | [Link](./day22_dp8_stock_final/README.md) | 冷冻期状态定义 / 通用解法 |
| **23** | Subsequence | 300. Longest Increasing Subseq (LIS)<br>674. Longest Continuous Incr Subseq<br>1143. Longest Common Subseq (LCS) | 🟡 | [Link](./day23_dp9/README.md) | **子序列(不连续) vs 子数组(连续)** |
| **24** | String_DP | 115.不同的子序列 (LIS)<br>583.两个字符串的删除操作<br>1035.不相交的线| 🟡<br>🔴🟡 | [Link](./day24_dp10_str/README.md) | **字符串dp** |
| **25** | String_DP2 | 72. 编辑距离 (Edit Distance)<br>647. 回文子串 (Palindromic Substrings)| 🔴🟡 | [Link](./day25_dp11/README.md) | **编辑距离/回文字符** |


*(持续更新中... Next: Edit Distance & Palindromes)*

## 🧠 算法模板精华 (Templates)

这里是我总结的“杀手锏”，用于应对面试中的常见模式：

- **[背包问题全家桶](./notes/dp_knapsack.md)**: 0-1背包(倒序)、完全背包(正序)、排列 vs 组合的遍历顺序总结。
- **[股票问题通解](./notes/dp_stock.md)**: 一个状态机模型解决 6 道股票题。
- **[回溯算法模板](./notes/backtracking.md)**: 包含去重 (`nums[i]==nums[i-1]`) 和剪枝技巧。
- **[二叉树遍历](./notes/binary_tree.md)**: 递归与迭代的统一写法，以及 LCA 问题的后序遍历思想。

## 🛠️ 工具与环境 (Tools)

- **IDE**: VS Code (LeetCode Extension)
- **Language**: Python 3
- **Environment**: WSL2 (Ubuntu) + Anaconda
- **Deploy**: Github Actions (Planned)

## 🤝 关于作者

- **School**: Sun Yat-sen University (SYSU)
- **Focus**: Deep Learning, NLP, Algorithm Design
- **Status**: 2027 Master Graduate (Expected)

---
*Last Updated: 2026-01-08*