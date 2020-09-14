"""
day: 2020-09-14
url: https://leetcode-cn.com/problems/squares-of-a-sorted-array/
题目名: 有序数组的平方
给定一个递增数组,返回每个数字的平方组成的新数组,也升序排列

示例:
    输入：[-4,-1,0,3,10]
    输出：[0,1,9,16,100]

思路:
    首先找到第一个不小于0的数的位置,那么对于这个数之后的数组的绝对值,都是升序的.
    对于这个数之前的数组的绝对值,倒序访问,就是升序的.所以可以定义两个指针,分别指向
    最后一个小于0的数与第一个不小于0的数,然后根据绝对值的大小交替计算.
"""
from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        right = 0
        res = []
        while right < n and A[right] < 0:
            right += 1
        left = right - 1
        while left >= 0 and right < n:
            if abs(A[left]) < abs(A[right]):
                res.append(A[left] * A[left])
                left -= 1
            else:
                res.append(A[right] * A[right])
                right += 1
        for i in range(left, -1, -1):
            res.append(A[i] * A[i])
        for i in range(right, n):
            res.append(A[i] * A[i])
        return res


if __name__ == "__main__":
    test = [-4, -1, 0, 3, 10]
    s = Solution()
    print(s.sortedSquares(test))
