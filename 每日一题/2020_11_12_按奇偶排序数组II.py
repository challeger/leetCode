"""
day: 2020-11-12
url: https://leetcode-cn.com/problems/freedom-trail/
题目名: 按奇偶排序数组 II
给定一个非负整数数组A, A 中一半整数是奇数,一半整数是偶数.

对数组进行排序,以便当 A[i] 为奇数时,i 也是奇数；当 A[i] 为偶数时, i 也是偶数.

你可以返回任何满足上述条件的数组作为答案.

思路:
双指针,一个指向奇数位,一个指向偶数位
每次找到不符合要求的偶数位,就找一个不符合要求的奇数位,将他们交换
"""
from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd_idx = 1
        n = len(A)
        for even_idx in range(0, n, 2):
            if A[even_idx] % 2:  # 索引为偶数,值为奇数
                while A[odd_idx] % 2:
                    odd_idx += 2
                A[even_idx], A[odd_idx] = A[odd_idx], A[even_idx]
        return A
