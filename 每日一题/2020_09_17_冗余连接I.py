"""
day: 2020-09-17
url: https://leetcode-cn.com/problems/redundant-connection/
题目名: 冗余连接
在本题中,树指的是一个连通且无环的无向图.
输出一个图,该图由一个有着N个节点(节点值不重复)的树及一条附加的边构成.附加的边的
两个顶点包含在1到N中间,这条附加的边不属于树中已存在的边.

结果图是一个以 边 组成的二维数组,每一条 边 的元素都是一堆[u, v],满足u < v,表示连接顶点
u和v的无向图的边.

返回一条可以删去的边,使得结果图是一个有着N个节点的树,如果有多个答案,则返回二维数组中最后出现
的边,答案边[u, v]应满足相同的格式 u < v
思路:
我们建立一个并查集,如果在建立的过程中,发现数组中的某一对元素具有相同的父节点,那么说明
这两个节点之间的边可以作为冗余边删除,因为他们之间是连通的,并且具有相同的父节点,也就可以通过
父节点连通,所以是冗余边,因为答案要求删除最后一条出现的冗余边,所以我们应该将数组遍历完,并用一个
变量记录最后出现的冗余边
"""
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 找到节点的父节点
        def find(x):
            if parents[x] == -1:
                return x

            return find(parents[x])

        idx = 0
        n = len(edges)
        parents = [-1 for _ in range(n+1)]
        for i in range(n):
            # 找到两个节点的父节点
            x_f = find(edges[i][0])
            y_f = find(edges[i][1])
            # 如果两个父节点相同,说明这两个节点是连通的
            # 而且因为他们原本就处于edges中,代表他们两个之间也存在一条边
            # 所以将这条边标记为要删除的边
            # 因为题目要求我们删除最后出现的边,所以要一直循环到结束.
            if x_f == y_f:
                idx = i
            # 如果不相同,因为edges[i][0]是与edges[i][1]连通的
            # 我们将0作为父节点来连通他们.
            else:
                parents[y_f] = x_f
        return edges[idx]
