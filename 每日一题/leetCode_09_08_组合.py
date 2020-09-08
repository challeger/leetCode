"""
day: 2020-09-08
url: https://leetcode-cn.com/problems/combinations/
题目名: 组合
给定两个整数n和k,返回1...n中所有可能的k个数的组合.
示例:
    输入: n=4, k=2
    输出:
    [
        [2, 4],
        [3, 4],
        [2, 3],
        [1, 2],
        [1, 3],
        [1, 4]
    ]
思路:
    对于C(n, k), 他只会有两种结果,
        1. 选中了n,那么剩下的就是C(n-1, k-1)
        2. 没选中n,那么剩下的就是C(n-1, k)
    所以C(n, k) = C(n-1, k-1) + C(n-1, k)
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n or k == 0:
            return []
        if k == 1:
            return [[i+1] for i in range(n)]
        if k == n:
            return [[i+1 for i in range(n)]]

        ans = self.combine(n-1, k)
        for item in self.combine(n-1, k-1):
            item.append(n)
            ans.append(item)
        return ans

    def combine_dfs(self, n: int, k: int) -> List[List[int]]:
        res = []
        if k > n or k == 0:
            return res

        def dfs(start, path):
            nonlocal res
            if len(path) == k:
                res.append(path)
                return
            # 搜索起点的上界 + 接下来要选择的元素个数 -1 = n
            # 接下来要选择的元素个数为 k - len(path)
            # 上界 = n - (k - len(path)) + 1
            # 因为从1开始,所以上界也要+1
            for i in range(start, n-(k-len(path))+2):
                path.append(i)
                dfs(i+1, path[:])
                path.pop()
        dfs(1, [])
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.combine_dfs(4, 2))
