"""
day: 2020-10-03
url: https://leetcode-cn.com/problems/two-sum/
题目名: 两数之和
给定一个整数数组 nums 和一个目标值 target,请你在该数组中找出和为目标值的那两个整数,并返回他们的数组下标.
你可以假设每种输入只会对应一个答案.但是,数组中同一个元素不能使用两遍
思路:
    ...
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {v: i for i, v in enumerate(nums)}
        for i, v in enumerate(nums):
            value = target - v
            if value in dic and i != dic[value]:
                return i, dic[value]
