"""
day: 2020-10-28
url: https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
题目名: 独一无二的出现次数
给你一个整数数组 arr,请你帮忙统计数组中每个数的出现次数

如果每个数的出现次数都是独一无二的,就返回 true；否则返回 false

思路:

用字典记录出现次数, 然后把values组成的列表的长度,与转为集合后的长度进行对比
如果不相同说明进行了去重,也就是为false,否则为true
"""
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for num in arr:
            dic[num] = dic.get(num, 0) + 1
        return len(dic.values()) == len(set(dic.values()))
