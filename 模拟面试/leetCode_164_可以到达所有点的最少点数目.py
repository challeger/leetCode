"""
day: 2020-09-12
url: https://leetcode-cn.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
题目名:可以到达所有点的最少点数目
给你一个有向无环图,n个节点编号为0到n-1,以及一个边数组edges,
其中edges[i]=[fromi, toi] 表示一条从点 fromi 到点 toi 的有向边.

找到最小的点集使得从这些点出发能到达图中所有点.题目保证解存在且唯一.

你可以以任意顺序返回这些节点编号
思路:
1. 贪心
    要想使用最小的点集,那么只要点集中的每一个点入度都为0即可.
"""
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nums = set(range(n))
        for start, end in edges:
            if end in nums:
                nums.remove(end)
        return list(nums)


if __name__ == "__main__":
    s = Solution()
    print(s.findSmallestSetOfVertices(
        6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]))
