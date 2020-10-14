"""
day: 2020-10-14
url: https://leetcode-cn.com/problems/find-common-characters/
题目名: 查找常用字符
给定仅有小写字母组成的字符串数组A,返回列表中的每个字符串中都显示的全部字符组成
的列表. 例如,如果一个字符在每个字符串中出现3次,但不是4次,则需要在最终答案中包含该字符
3次

思路:
    以第一个字符串为基准,获取在该字符串中的所有字符,然后依次判断每个字符
    在所有字符串中出现的最小次数, 然后添加到结果中
"""
from typing import List
from functools import reduce
from collections import Counter


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = []
        if not A:
            return res
        key = set(A[0])
        for k in key:
            min_num = min(a.count(k) for a in A)  # 得到每个字符的最小出现次数
            res += min_num * k  # 添加到结果中
        return res

    def commonChars_1(self, A: List[str]) -> List[str]:
        return list(reduce(lambda x, y: x & y, map(Counter, A)).elements())
