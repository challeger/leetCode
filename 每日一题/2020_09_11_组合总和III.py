"""
day: 2020-09-11
url: https://leetcode-cn.com/problems/combination-sum-iii/
题目名: 组合总和III
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
示例:
    输入: k = 3, n = 7
    输出: [[1,2,4]]
思路:
    
"""
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        l = 9
        nums = [i for i in range(1, l+1)]
        ans = []

        def dfs(start, target, path):
            if target == 0 and len(path) == k:
                ans.append(path)
            for i in range(start, l):
                if nums[i] > target or len(path) == k:
                    break
                path.append(nums[i])
                dfs(i+1, target-nums[i], path[:])
                path.pop()

        dfs(0, n, [])
        return ans
