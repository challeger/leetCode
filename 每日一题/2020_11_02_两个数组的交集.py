"""
day: 2020-11-02
url: https://leetcode-cn.com/problems/intersection-of-two-arrays/
题目名: 两个数组的交集

给定两个数组,编写一个函数来计算它们的交集

"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)
