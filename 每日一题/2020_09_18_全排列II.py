"""
day: 2020-09-18
url: https://leetcode-cn.com/problems/permutations-ii/
题目名: 全排列II
给定一个可包含重复数字的序列,返回所有不重复的全排列

示例:
    输入: [1, 1, 2]
    输出:
    [
        [1, 1, 2],
        [1, 2, 1],
        [2, 1, 1]
    ]
思路:
    为了避免出现重复的排列,我们应该记录在每次排列中元素的使用情况
    首先需要将数组进行排序,然后依次遍历数组去建立排列,如果当前的数字
    与前一个数字相等,并且前一个数字的没有被使用,这并不是说明我们需要将
    当前的数字进行排列,恰恰相反,正是因为前一个数字的状态是False,说明
    当前的循环是前一个数字的排列结束之后,新开启的一个循环,所以我们应该跳过
    本次循环.
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 对数组进行排序
        n = len(nums)  # 记录数组的长度
        checked = [False] * n  # 记录数组中数字的使用情况,默认是False
        res = []  # 结果数组

        def backtrack(path):
            if len(path) == n:
                res.append(path)
                return
            for i in range(n):
                if checked[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not nums[i-1]:
                    continue
                checked[i] = True
                path.append(nums[i])
                backtrack(path[:])
                path.pop()
                checked[i] = False

        backtrack([])
        return res
