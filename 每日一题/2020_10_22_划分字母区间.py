"""
day: 2020-10-22
url: https://leetcode-cn.com/problems/partition-labels/
题目名: 划分字母区间
字符串 S 由小写字母组成.
我们要把这个字符串划分为尽可能多的片段,同一个字母只会出现在其中的一个片段.
返回一个表示每个字符串片段的长度的列表. 

示例:

    输入: S = "ababcbacadefegdehijhklij"
    输出: [9, 7, 8]
    解释: 划分结果为 'ababcbaca', 'defegde', 'hijhklij'

思路:
    记录每个字母出现的最后位置,然后从头开始遍历字符串,用一个指针r指向当前遍历
    过的字符中,最远距离的索引.如果某次遍历,当前索引与r相等,那么说明当前r就是能
    划分的最小区间了,就将其加入答案中,再开始下一次遍历
"""
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        res = []
        l = r = 0
        last = {c: idx for idx, c in enumerate(S)}
        for idx, c in enumerate(S):
            r = max(r, last[c])
            if r == idx:
                res.append(r-l+1)
                l = idx + 1
        return res
