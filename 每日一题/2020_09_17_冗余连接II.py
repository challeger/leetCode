"""
day: 2020-09-17
url: https://leetcode-cn.com/problems/redundant-connection-ii/
题目名: 冗余连接
在本题中,有根树指满足以下条件的有向图

该树只有一个根节点,所有其他节点都是该根节点的后继,
每一个节点只有一个父节点,根节点没有父节点.

输出一个有向图,该图由一个有着N个节点(节点值不重复)的树及一条附加的边构成.附加的边的
两个顶点包含在1到N中间,这条附加的边不属于树中已存在的边.

结果图是一个以 边 组成的二维数组,每一条 边 的元素都是一堆[u, v],满足u < v,用以表示有向图中
连接顶点u和顶点v的边,其中u是v的一个父节点

返回一条可以删去的边,使得结果图是一个有着N个节点的有根树,如果有多个答案,则返回二维数组中最后出现
的边
思路:
我们建立一个并查集,如果在建立的过程中,发现数组中的某一对元素具有相同的父节点,那么说明
这两个节点之间的边可以作为冗余边删除,因为他们之间是连通的,并且具有相同的父节点,也就可以通过
父节点连通,所以是冗余边,因为答案要求删除最后一条出现的冗余边,所以我们应该将数组遍历完,并用一个
变量记录最后出现的冗余边
"""
from typing import List


class UnionFind:
    def __init__(self, n):
        # 每个人默认的父节点都是自己
        self.ancestor = list(range(n))

    def union(self, index1: int, index2: int):
        # 找到index1的父节点,index2的父节点,并在一起
        self.ancestor[self.find(index1)] = self.find(index2)

    def find(self, index: int) -> int:
        if self.ancestor[index] != index:
            self.ancestor[index] = self.find(self.ancestor[index])
        return self.ancestor[index]


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        nodesCount = len(edges)
        uf = UnionFind(nodesCount + 1)
        parent = list(range(nodesCount + 1))
        conflict = -1
        cycle = -1
        for i, (node1, node2) in enumerate(edges):
            # 如果此时node2的父节点不是自己
            # 那么说明除了node1以外,还有一个节点是node2的父节点
            # 也就是产生了冲突,将这条边标记
            if parent[node2] != node2:
                conflict = i
            else:
                parent[node2] = node1
                # 如果node1是node2的父节点,且node1与node2具有相同的父节点
                # 说明这两个节点在环内,记录环最后出现的位置
                if uf.find(node1) == uf.find(node2):
                    cycle = i
                else:
                    # 不相同,则将他们并在一起
                    uf.union(node1, node2)

        # 如果没有出现冲突的边(环路边指向了根节点),那么说明附加的边一定导致环路出现
        # 并且是在最后出现的, 那么就删除导致出现环路的边
        if conflict < 0:
            return [edges[cycle][0], edges[cycle][1]]
        else:
            # 如果有出现冲突的边,那么需要判断是否出现了环路
            conflictEdge = edges[conflict]
            # 出现了环路, 那么附加的边不可能是导致出现环路的边
            # 因为一条边不可能同时被标记为出现环路和导致冲突
            # 所以附加的边一定是node2与它被记录的父节点.
            if cycle >= 0:
                return [parent[conflictEdge[1]], conflictEdge[1]]
            # 如果没有出现环路,那么附加的边就是当前导致冲突的边
            else:
                return [conflictEdge[0], conflictEdge[1]]
