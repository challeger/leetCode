"""
day: 2020-10-25
url: https://leetcode-cn.com/problems/longest-mountain-in-array/
题目名: 数组中的最长山脉
我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：
B.length >= 3
存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
（注意：B 可以是 A 的任意子数组，包括整个数组 A。）

给出一个整数数组 A，返回最长 “山脉” 的长度。
如果不含有 “山脉” 则返回 0。

示例:

    输入: [2,1,4,7,3,2,5]
    输出: 5
    解释: 1,4,7,3,2

    输入: [2,2,2]
    输出: 0
思路:
    遍历数组,如果是处于上升沿,首先判断前面一节是否是上升沿,不是则更新山脉的起点.

    如果处于下降沿, 就判断当前的山脉长度和res中保存的最长长度,取最大值

    否则就重置山脉的起点
"""
from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        start = -1  # 山脉的起点
        res = 0
        for i in range(1, n):
            if A[i] > A[i-1]:
                if i == 1 or A[i-2] >= A[i-1]:
                    start = i - 1
            elif A[i-1] > A[i]:
                if start != -1:
                    res = max(res, i-start+1)
            else:
                start = -1
        return res
