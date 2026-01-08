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
├── 📂 day15_dp_basics/
│   ├── ...
├── 📂 notes/                  # 🧠 核心资产：通用算法模板
│   ├── binary_search_template.md
│   ├── knapsack_problem_summary.md
│   └── sliding_window_patterns.md
└── README.md                  # 项目主页
```

## 🗓️ 刷题进度 (Progress)

| Day | Topic (专题) | Problems (题目) | Difficulty | Solution & Notes | Key Takeaways (核心考点) |
|:---:|:---|:---|:---:|:---:|:---|
| 01 | Array / HashMap | [1. Two Sum](https://leetcode.cn/problems/two-sum/) | 🟢 | [Link](./day01/README.md) | 哈希表空间换时间 |
| 04 | Linked List | [206. Reverse List](https://leetcode.cn/problems/reverse-linked-list/) | 🟢 | [Link](./day04/README.md) | 双指针迭代 / 递归 |
| 14 | Greedy | [56. Merge Intervals](https://leetcode.cn/problems/merge-intervals/) | 🟡 | [Link](./day14/README.md) | 区间排序策略 |
| 16 | DP - Knapsack | [416. Partition Equal Subset Sum](https://leetcode.cn/problems/partition-equal-subset-sum/) | 🟡 | [Link](./day16/README.md) | 0-1背包一维优化 |
| ... | ... | ... | ... | ... | ... |

*(持续更新中...)*

## 🧠 算法模板精华 (Templates)

这里是我总结的“杀手锏”，用于应对面试中的常见模式：

- **[二分查找通用模板](./notes/binary_search.md)**: 解决 `left < right` 还是 `left <= right` 的死循环问题。
- **[回溯算法三部曲](./notes/backtracking.md)**: 排列、组合、子集问题的通用解法。
- **[背包问题全家桶](./notes/knapsack.md)**: 0-1背包、完全背包的遍历顺序总结。
- **[滑动窗口](./notes/sliding_window.md)**: 解决子串搜索问题的固定套路。

## 🛠️ 工具与环境 (Tools)

- **IDE**: VS Code (配合 LeetCode 插件进行本地调试)
- **Language**: Python 3
- **Version Control**: Git & GitHub
- **Visualization**: 使用 WandB / Matplotlib 进行部分算法的可视化分析 (如果有)

## 🤝 关于作者

- **School**: Sun Yat-sen University (SYSU)
- **Major**: Logic & Computer Science
- **Focus**: Deep Learning, NLP, Algorithm Design

---
*Last Updated: 2026-01-08*

