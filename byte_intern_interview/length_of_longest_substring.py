# 3.无重复字符的最长子串
from typing import List,Dict,Optional
import collections

def length_of_longest_substring(s:str) -> int:
    """
    使用滑动窗口解决，时间复杂度O(N),空间复杂度为O(k),k为s中不同字符的个数
    """
    # 边界判断，若字符串为空，则返回0
    if not s: # 空值判断O(1)
        return 0 # 返回值O(1)
    
    dic = {} # 哈希表创立O(1)
    left = 0 #赋值操作O(1)
    max_length = 0 #赋值操作O(1)

    for right,char in enumerate(s):# 循环操作O(n)
        if char in dic and dic[char] >= left: #哈希表判断键和哈希表取值比较大小O(1)
            left = dic[char] + 1 # 赋值操作O(1)
        dic[char] = right # 赋值操作O(1)
        max_length = max(max_length,right - left + 1) # 赋值与比较大小操作O(1)
    
    return max_length # 返回值O(1)

s = 'abcabcaa'
print(length_of_longest_substring(s))