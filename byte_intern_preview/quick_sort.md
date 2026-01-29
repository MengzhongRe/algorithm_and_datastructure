# 🚀 算法笔记：快速排序 (Quick Sort) - 双指针原地版

**核心思想：** 分治法 (Divide and Conquer)
**逻辑本质：** 通过一趟排序将待排记录分割成独立的两部分，其中一部分记录的关键字均比另一部分记录的关键字小，则可分别对这两部分记录继续进行排序。

---

## 1. 完整代码模板 (Python)

```python
import random
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        主函数入口
        """
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, nums: List[int], start: int, end: int):
        """
        快排递归函数
        :param nums: 数组
        :param start: 当前处理区间的起始索引
        :param end: 当前处理区间的结束索引
        """
        # 1. 递归终止条件 (Base Case)
        # 当区间只有一个元素，或区间不存在(start > end)时，停止
        if start >= end:
            return

        # 2. 随机选基准并交换到头部 (打破有序数组的 O(N^2) 诅咒)
        rand_idx = random.randint(start, end)
        nums[start], nums[rand_idx] = nums[rand_idx], nums[start]
        
        # 3. 设定基准 (Pivot) 和 双指针
        pivot = nums[start]
        left = start
        right = end

        # 4. Partition 核心逻辑 (哨兵探测)
        while left < right:
            # 【关键点 A】必须先动右指针 (Right Sentinel)
            # 寻找比 pivot 小的数
            while left < right and nums[right] >= pivot:
                right -= 1
            
            # 【关键点 B】再动左指针 (Left Sentinel)
            # 寻找比 pivot 大的数
            while left < right and nums[left] <= pivot:
                left += 1
            
            # 交换两个不符合规矩的元素
            nums[left], nums[right] = nums[right], nums[left]

        # 5. 基准归位
        # 此时 left == right，且 nums[left] 一定 <= pivot
        # 将基准值从“裁判席”(start) 交换到“分界线”(left)
        nums[start], nums[left] = nums[left], nums[start]

        # 6. 递归处理左右两边
        # 注意：中间的 left 位置已经是排好序的 pivot，不需要再动
        self.quick_sort(nums, start, left - 1)
        self.quick_sort(nums, left + 1, end)
```

---

## 2. 算法整体逻辑解析

我们将排序过程看作是一个**“寻找基准值正确位置”**的过程。

1.  **选定裁判 (Pivot Selection):**
    *   为了方便操作，我们先**随机**选一个人当裁判，并把他请到**第一个位置** (`start`) 坐好。
    *   *逻辑目的：* 固定不变量，防止裁判在后续的交换中“走丢”。

2.  **两头围堵 (Two-Pointer Scan):**
    *   **右哨兵 (`right`)** 从右往左走，负责抓**比裁判小**的人。
    *   **左哨兵 (`left`)** 从左往右走，负责抓**比裁判大**的人。
    *   当两人都抓到时，让他们**互换位置**。
    *   *逻辑目的：* 把小的扔左边，大的扔右边。

3.  **裁判归位 (Pivot Homing):**
    *   当左右哨兵**相遇**时，说明搜索结束。相遇点就是分界线。
    *   此时，把坐在第一个位置的裁判 (`nums[start]`) 请下来，放到相遇点 (`nums[left]`)。
    *   *结果：* 裁判左边全是小的，右边全是大的。

4.  **分而治之 (Divide & Conquer):**
    *   裁判的位置已经固定了，不用再动。
    *   对**左边那堆人**和**右边那堆人**，重复上述步骤。

---

## 3. ☠️ 易错点、注意点与边界条件 (生死线)

面试时，代码能不能跑通，全看这几个细节：

### ① 为什么内层 `while` 必须有 `left < right`？
*   **代码：** `while left < right and nums[right] >= pivot:`
*   **原因：** 防止指针**冲出边界**。
*   **逻辑：** 如果数组是 `[1, 1, 1]`，如果没有 `left < right`，`right` 指针会一路减到 `-1`，导致 `IndexError`。

### ② 为什么必须带等号 (`>=` 和 `<=`)？
*   **代码：** `nums[right] >= pivot`
*   **原因：** 防止**死循环**。
*   **逻辑：** 如果数组是 `[5, 5, 5]`，且 `pivot=5`。
    *   如果不带等号：`right` 发现 5 不大于 5，停下；`left` 发现 5 不小于 5，停下。
    *   交换 5 和 5。
    *   下一轮循环，指针依然停在原地，无限交换，程序卡死。

### ③ 为什么要 **先动右指针** (`right`)？
*   **前提：** 我们的基准 `pivot` 在最左边 (`start`)。
*   **原因：** 确保最后相遇的位置的值 **<= pivot**。
*   **推演：**
    *   如果右指针先走，它停下的位置一定是**比 pivot 小**的数（或者回到了 left）。
    *   最后一步 `nums[start], nums[left] = nums[left], nums[start]` 交换时，我们是把一个**小数**换到了最左边，这是安全的。
    *   *反之：* 如果左指针先走，它可能会停在一个**大数**上。最后交换时，会把大数换到最左边，这就破坏了“左边比 pivot 小”的规则。

### ④ 为什么要随机化 (`random.randint`)？
*   **原因：** 对抗**最坏情况**。
*   **逻辑：** 如果数组已经有序 `[1, 2, 3, ... 10000]`，每次选第一个数做 pivot，左边分到 0 个，右边分到 N-1 个。
    *   递归树退化成链表。
    *   时间复杂度退化为 $O(N^2)$，导致超时。

### ⑤ 递归范围的边界 (`left-1` 和 `left+1`)
*   **代码：** `quick_sort(..., start, left - 1)` 和 `quick_sort(..., left + 1, end)`
*   **原因：** `left` 位置是归位后的 pivot，它已经排好序了。
*   **易错：** 不要写成 `quick_sort(..., start, left)`，否则会死循环。

---

## 4. 复杂度分析 (背诵)

*   **时间复杂度：**
    *   平均：$O(N \log N)$
    *   最坏：$O(N^2)$ (不加随机化且数组有序时)
*   **空间复杂度：**
    *   平均：$O(\log N)$ (递归栈的深度)
    *   最坏：$O(N)$ (递归树退化为链表)
*   **稳定性：** **不稳定** (交换过程会打乱相同元素的相对位置)。

---

### 🚀 助记口诀

> **随机基准换排头，**
> **左`i`右`j`两边走。**
> **基准在左右先动，**
> **找小找大换个够。**
> **相遇之处基准坐，**
> **递归左右不用愁。**