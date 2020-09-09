"""
day: 2020-09-09
url: https://leetcode-cn.com/problems/combination-sum/
题目名: 组合总和
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
示例:
    输入: candidates = [2,3,6,7], target = 7,
    输出:
    [
        [7],
        [2,2,3]
    ]
思路:
    我们首先将数组进行排序,这样我们在遍历数组时,如果某次遍历的数
    已经大于当前的剩余值.那么说明他后面的所有数都不满足我们的结果,那么就
    可以直接结束这次循环.

    为了去重,我们在遍历数组时,定义一个start,每次就从上次搜索的位置开始进行
    下一次搜索,这样就不会出现重复的组合了.
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res = []

        def dfs(start, balance, path):
            # 剩余的值为0,说明找到了一个正确的答案
            if balance == 0:
                res.append(path)

            for i in range(start, n):
                foo = balance-candidates[i]
                # 因为是一个有序数组,如果当前数字已经超过了剩余的和,那么后面的数字都不是有效的
                if foo < 0:
                    break
                path.append(candidates[i])
                # 从本次符合要求的数开始下一次搜索,因为数是可以重复使用的.
                dfs(i, foo, path[:])
                # 回溯状态
                path.pop()

        dfs(0, target, [])
        return res


if __name__ == "__main__":
    test = [2, 3, 6, 7]
    s = Solution()
    print(s.combinationSum(test, 7))
