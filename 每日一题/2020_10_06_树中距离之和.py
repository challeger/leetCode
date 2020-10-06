"""
day: 2020-10-06
url: https://leetcode-cn.com/problems/sum-of-distances-in-tree/
题目名: 树中距离之和
给定一个无向、连通的树,树中有 N 个标记为 0...N-1 的节点以及 N-1 条边,
第 i 条边连接节点 edges[i][0] 和 edges[i][1],

返回一个表示节点 i 与其他所有节点距离之和的列表 ans,
思路:
    我们通过dfs获取所有节点的深度 与 每个节点的子节点数(包括自己)
    那么根节点的距离之和就是 所有节点的深度之和

    那么根节点的子节点的距离之和,应该是

    因为往下走了一层,所以到达其他非自己子节点的节点的距离 + 1
    也就是 ans[root] + N - count[son]
    而且对于自己的子节点,往下走了一层,那么到达这些节点的距离就 -1
    也就是 ans[root] + N - 2 * count[son]
"""
from typing import List


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        tree = [[] for _ in range(N)]
        for baba, erza in edges:
            tree[baba].append(erza)
            tree[erza].append(baba)
        # 记录每个节点的深度
        depth = [0 for _ in range(N)]
        # 每个节点的子节点数(包括自身)
        count = [0 for _ in range(N)]

        def dfsForDepthAndCount(node, father):
            # 子节点数量包含自己,所以初值为1
            count[node] = 1
            for son in tree[node]:
                # 不是父节点,就只能是子节点了
                if son != father:
                    # 子节点的深度都是当前节点的深度+1
                    depth[son] = depth[node] + 1
                    # dfs找所有子节点的的子节点数
                    dfsForDepthAndCount(son, node)
                    # 当前节点的子节点数是 子节点的子节点数之和
                    count[node] += count[son]

        # 从根节点开始
        dfsForDepthAndCount(0, -1)
        answer = [0 for _ in range(N)]
        # 根节点的答案就是各节点深度之和
        answer[0] = sum(depth)

        def dfsForAnswer(node, father):
            for son in tree[node]:
                if son != father:
                    # 根据当前节点的距离之和,可以算出它的所有子节点的距离之和
                    answer[son] = answer[node] + N - 2 * count[son]
                    dfsForAnswer(son, node)

        dfsForAnswer(0, -1)
        return answer
