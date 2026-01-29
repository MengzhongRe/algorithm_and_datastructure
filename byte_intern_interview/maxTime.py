# 统计给定字符串中出现的次数最多的字符及其出现次数
from typing import Tuple,List,Optional

def maxTime(s:str) -> Optional[Tuple[List[str],int]]:
    """
    # 用哈希表记录每个字符出现的次数，时间复杂度为O(N),空间复杂度为O(k),k为s中不同字符的个数
    """
    # 边界判断：
    if not s: # 判断操作O(1)
        return None # 返回操作O(1)
    
    dic = {} # 先创建一个哈希表 # 赋值操作O(1)

    for char in s: # 遍历所有字符 O(n)
        if char not in dic: # 需要为新出现的char赋值 哈希表判断O(1)
            dic[char] = 1 # 哈希表赋值 O(1)
        else: # 非首次遇到的char直接将其值+1即可
            dic[char] += 1 # 哈希表赋值 O(1)
    
    max_count = max(dic.values()) # 遍历哈希表的值列表并取最大值，O(k)
    max_chars = [char for char,time in dic.items() if time == max_count]#  O(k)
    # 由于最多出现的字符可能不只一个，所以我们用列表推导式遍历哈希表的键值对，判断若值等于最大值则收录在列表当中。

    return max_chars,max_count # 返回值O(1)

s = 'abcabbd'
b = ''
print(maxTime(b))

# 用python原生库实现collections.Counter实现简化
from typing import List,Tuple,Optional
from collections import Counter

def maxTime(s:str) -> Optional[Tuple[List[str],int]]:
    """
    maxTime 的 Docstring
    # 用python原生库实现collections.Counter实现简化，复杂度一样
    :param s: 说明
    :type s: str
    :return: 说明
    :rtype: Tuple[List[str], int] | None
    """
    if not s:
        return None
    
    dic = Counter(s) # 实现了字符s的计数统计，底层还是哈希表

    max_count = max(dic.values())
    max_chars = [char for char,count in dic.items() if count == max_count]

    return max_chars,max_count


