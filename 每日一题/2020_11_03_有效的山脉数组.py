"""
day: 2020-11-03
url: https://leetcode-cn.com/problems/valid-mountain-array/
题目名: 有效的山脉数组
给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。

让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：
    A.length >= 3
        在 0 < i < A.length - 1 条件下，存在 i 使得：
        A[0] < A[1] < ... A[i-1] < A[i]
        A[i] > A[i+1] > ... > A[A.length - 1]
"""
from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        l, r = 0, len(A)-1
        while l < r and A[l] < A[l+1]: l += 1
        while l < r and A[r] < A[r-1]: r -= 1
        return l == r and l != 0 and r != len(A)-1
