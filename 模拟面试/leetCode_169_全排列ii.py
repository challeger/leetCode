"""
day: 2020-09-14
url: https://leetcode-cn.com/problems/permutations-ii/
题目名: 全排列II
给定一个可包含重复数字的序列,返回所有不重复的全排列

示例:
    输入: [1,1,2]
    输出:
    [
        [1,1,2],
        [1,2,1],
        [2,1,1]
    ]
思路:
    dfs,回溯,剪枝去重.
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        check = [False for _ in range(n)]
        nums.sort()

        def backtrack(path):
            if len(path) == n:
                res.append(path)
            for i in range(n):
                if check[i]:
                    continue
                # 如果前一个数没被使用,说明它已经被使用了,但是被撤销了,也就是
                # 那一次的dfs已经全部完成,那么本次就可以跳过
                # 若为1说明还在dfs的过程中,需要继续走..
                if i > 0 and nums[i] == nums[i-1] and check[i-1] == 0:
                    continue
                check[i] = True
                path.append(nums[i])
                backtrack(path[:])
                path.pop()
                check[i] = False
        backtrack([])
        return res
