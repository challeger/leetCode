"""
day: 2020-10-16
url: https://leetcode-cn.com/problems/squares-of-a-sorted-array/
题目名: 有序数组的平方
给定一个按非递减顺序排序的整数数组 A,返回每个数字的平方组成的新数组,要求也按非递减顺序排序

注意:
    整数数组包括负数
思路:
双指针:
    找到第一个不小于0的数,作为右指针,该指针左边一个数为左指针,
    比较两个指针指向的值的绝对值的大小,然后依次加到新数组中
"""
from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A:
            return None
        n = len(A)
        right = 0  # 找到第一个不小于0的数
        while right < n and A[right] < 0:
            right += 1
        left = right - 1
        res = []
        while left >= 0 and right < n:
            if abs(A[left]) > abs(A[right]):
                res.append(A[right] * A[right])
                right += 1
            else:
                res.append(A[left] * A[left])
                left -= 1
        while left >= 0:
            res.append(A[left] * A[left])
            left -= 1

        while right < n:
            res.append(A[right] * A[right])
            right += 1
        
        return res
