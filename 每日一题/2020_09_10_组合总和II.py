"""
day: 2020-09-10
url: https://leetcode-cn.com/problems/combination-sum-ii/
题目名: 组合总和II
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在组合中只能使用一次

    解集不能包含重复的组合
示例:
    输入: candidates = [10,1,2,7,6,1,5], target = 8,
    输出:
    [
        [1, 7],
        [1, 2, 5],
        [2, 6],
        [1, 1, 6]
    ]
思路:
    我们首先将数组进行排序,这样我们在遍历数组时,如果某次遍历的数
    已经大于当前的剩余值.那么说明他后面的所有数都不满足我们的结果,那么就
    可以直接结束这次循环.

    为了去重,我们在遍历数组时,定义一个start,每次就从上次选用的位置的下一位开始进行
    下一次搜索,同时如果本次选择的数字与上一个数字相等,就跳过本次循环.
    这样就不会出现重复的组合了.
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 方案1, 集合去重
        candidates.sort()
        n = len(candidates)
        res = []

        def dfs(balance, start, path):
            if balance == 0:
                res.append(path)

            for i in range(start, n):
                if candidates[i] > balance:
                    break
                # 方案2, 如果本次要添加的数字与上次添加的数字相同,那么就跳过
                if i != start and candidates[i-1] == candidates[i]:
                    continue
                path.append(candidates[i])
                dfs(balance-candidates[i], i+1, path[:])
                path.pop()

        dfs(target, 0, [])
        return res
