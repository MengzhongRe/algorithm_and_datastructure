# 📝 ByteDance AIGC Algorithm Interview Code Review

- **Date:** 2026-01-29
- **Type:** Technical Interview (Round 1)
- **Tag:** #PyTorch #Transformer #SlidingWindow #HashMap

---

## 📖 Introduction

本文总结了在字节跳动 AIGC 算法实习生面试中遇到的三道核心编程题。通过复盘，旨在深入理解 **Transformer 底层实现机制** 以及 **经典算法题的边界条件处理**。

---

## 1. 🔥 Hard: 手写多头自注意力机制 (Multi-Head Self-Attention)

### 1.1 题目描述
不使用 `torch.nn.MultiheadAttention` API，仅使用 PyTorch 基础算子（Linear, matmul, softmax），实现一个标准的 Multi-Head Self-Attention 模块。

### 1.2 逻辑推演 (Mathematical Logic)
Attention 的本质是将输入映射到三个空间（Query, Key, Value），通过计算 Q 和 K 的相似度来对 V 进行加权。
多头（Multi-Head）则是将高维特征空间 $d_{model}$ 切分为 $h$ 个子空间，让模型并行捕捉不同层面的语义关联。

**核心公式：**
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
$$head_{dim} = dim // heads$$
**张量变换流 (Tensor Flow):**
1.  **Input:** `[Batch, Seq_Len, Dim]`
2.  **Split Heads:** `[Batch, Seq_Len, Heads, Head_Dim]` 
3.  **Transpose:** `[Batch, Heads, Seq_Len, Head_Dim]` (为了并行计算 QK^T)
4.  **Scaled Dot-Product:** 得到 Attention Score
5.  **Concat:** 恢复为 `[Batch, Seq_Len, Dim]`

### 1.3 标准代码实现 (PyTorch)

```python
import torch
import torch.nn as nn
import math

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model: int, num_heads: int):
        super().__init__()
        assert d_model % num_heads == 0, "d_model must be divisible by num_heads"
        
        self.d_model = d_model
        self.num_heads = num_heads
        self.head_dim = d_model // num_heads
        
        # 定义线性投影层 W_q, W_k, W_v, W_o
        self.w_q = nn.Linear(d_model, d_model)
        self.w_k = nn.Linear(d_model, d_model)
        self.w_v = nn.Linear(d_model, d_model)
        self.w_o = nn.Linear(d_model, d_model)

    def forward(self, x, mask=None):
        """
        x: [batch_size, seq_len, d_model]
        mask: [batch_size, 1, 1, seq_len] or [seq_len, seq_len] (Optional)
        """
        batch_size, seq_len, _ = x.shape
        
        # 1. 线性变换 (Linear Projections)
        Q = self.w_q(x)
        K = self.w_k(x)
        V = self.w_v(x)
        
        # 2. 分头与转置 (Split Heads & Transpose)
        # view: [b, s, h, d_k] -> transpose: [b, h, s, d_k]
        # 这样做的目的是让 Head 维度在 Seq 维度之前，以便最后两维做矩阵乘法
        Q = Q.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        K = K.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        V = V.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        
        # 3. 计算注意力分数 (Scaled Dot-Product)
        # scores shape: [b, h, s, s]
        # K.transpose(-2, -1) 是为了将最后两个维度转置以便相乘
        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.head_dim)
        
        # (可选) Mask 机制：将不需要关注的位置设为负无穷
        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)
            
        # 4. 归一化 (Softmax)
        attn_weights = torch.softmax(scores, dim=-1)
        
        # 5. 加权求和 (Weighted Sum)
        # [b, h, s, s] @ [b, h, s, d_k] -> [b, h, s, d_k]
        context = torch.matmul(attn_weights, V)
        
        # 6. 拼接与输出 (Concat & Final Linear)
        # transpose: [b, s, h, d_k] -> reshape: [b, s, d_model]
        context = context.transpose(1, 2).contiguous().view(batch_size, seq_len, self.d_model)
        
        return self.w_o(context)
```

### 1.4 易错点复盘
- **Transpose vs View:** 分头后必须先 `transpose` 交换维度，不能直接 `view`，否则语义会错乱。
- **Contiguous:** 调用 `view` 之前如果进行过转置，张量内存不连续，必须调用 `.contiguous()`。
- **Scaling:** 忘记除以 $\sqrt{d_k}$ 会导致 Softmax 处于饱和区，梯度消失。

---

## 2. 🟢 Easy: 统计出现次数最多的字符

### 2.1 题目描述
给定一个字符串，返回出现次数最多的字符及其次数。

### 2.2 核心思路
这是一个典型的 **哈希表 (Hash Map)** 应用题。时间复杂度应为 $O(N)$。

### 2.3 代码实现

**方案 A：Pythonic 写法 (推荐)**
利用 `collections.Counter`，代码极其简洁，体现对标准库的熟悉。

```python
from collections import Counter
from typing import List,Tuple,Optional

def max_frequent_char(s: str) -> Optional[Tuple[List[str],int]]:
    if not s:
        return None
    
    # 1. 计数
    counts = Counter(s)
    
    # 2. 获取 Top 1
    # most_common(1) 返回列表：[('a', 5)]
    char, count = counts.most_common(1)[0]
    return char, count
```

**方案 B：原生字典写法 (展示基本功)**

```python
from typing import List,Tuple,Optional

def max_frequent_char_manual(s: str) -> Optional[Tuple[List[str],int]]:
    if not s:
        return None
        
    counts = {}

    for char in s:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    
    max_count = max(counts.values())
    max_chars = [char for char,count in counts.items() if count == max_count]

    return max_chars,max_counts 
```

---

## 3. 🟡 Medium: 无重复字符的最长子串 (LeetCode 3)

### 3.1 题目描述
给定一个字符串 `s` ，找出其中不含有重复字符的 **最长子串** 的长度。

### 3.2 核心思路：优化滑动窗口
- **双指针:** `left` (窗口左边界), `right` (扫描指针)。
- **哈希表:** 记录字符**上一次出现的位置索引**。
- **跳跃逻辑:** 当 `right` 遇到重复字符时，不需要一步步收缩 `left`，而是直接将 `left` **瞬移** 到重复字符的下一位。

### 3.3 代码实现

```python
def length_of_longest_substring(s: str) -> int:
    # 记录字符最后一次出现的索引
    dic = {}
    left = 0
    max_len = 0
    
    for right, char in enumerate(s):
        # 核心判断：字符出现过，且出现的位置在当前窗口内 (>= left)
        if char in dic and dic[char] >= left:
            # 左边界直接跳跃到重复字符的右边
            left = dic[char] + 1
        
        # 更新字符的最新位置
        dic[char] = right
        
        # 计算当前合法窗口长度
        max_len = max(max_len, right - left + 1)
        
    return max_len
```

### 3.4 关键细节
- **判定条件:** `dic[char] >= left` 是必须的。因为 `dic` 存的是所有历史记录，如果一个字符上次出现在 `left` 左边，说明它已经被移出窗口了，不应该触发跳跃。
- **复杂度:** 时间 $O(N)$，空间 $O(|\Sigma|)$ (字符集大小)。

---

## 💡 总结 (Takeaway)

1.  **大模型岗位必须精通 PyTorch:** 能够手写 Attention、MLP、LayerNorm 是底线。不要只依赖 `transformers` 库。
2.  **基础数据结构不能忘:** 即使是简单的哈希表计数，也要写得规范、处理边界条件（如空串）。
3.  **算法题注重逻辑优化:** 滑动窗口的由“步进”到“跳跃”的优化，是体现算法思维的关键。