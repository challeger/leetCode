"""
day: 2020-09-07
url: https://leetcode-cn.com/problems/kth-ancestor-of-a-tree-node/
题目名: 树节点的第k个祖先
给你一棵树,树上有 n 个节点,按从 0 到 n-1 编号.树以父节点数组的形式给出,其中 parent[i] 是节点 i 的父节点.
树的根节点是编号为 0 的节点.

请你设计并实现 getKthAncestor(int node, int k) 函数,函数返回节点 node 的第 k 个祖先节点.
如果不存在这样的祖先节点，返回 -1 .

树节点的第 k 个祖先节点是从该节点到根节点路径上的第 k 个节点.
思路:
dp倍增:
    我们用dp[i][j]来表示 节点i的第2^j个父节点.
    dp[i][j] = dp[dp[i][j-1]][j-1]  --> 2^j = 2^(j-1) + 2^(j-1)
    那么当我们要查找节点node的第k个父节点时, 将k转为对应的二进制:
    例如 10 -> 1010, 那么我们从它的最高位开始, 依次访问dp, 对于node
    的第10个父节点, 就是node的第2^3个父节点 + 该父节点的第 2^1 个父节点.
"""
from typing import List


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.cols = 20
        self.dp = [[-1]*self.cols for _ in range(n)]
        for i in range(n):
            self.dp[i][0] = parent[i]
        # dp[i][j] 表示 节点i的第2^j个祖先
        for j in range(1, self.cols):
            for i in range(n):
                if self.dp[i][j-1] != -1:
                    # 节点i的第2^j个祖先,是它的第2^(j-1)个祖先节点的第2^(j-1)个祖先节点
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(self.cols-1, -1, -1):
            # 从k的最高为开始找
            # 比如k = 10 = 1010, 那么他的第10个父节点应该是 dp[[node][2^3]][2^1]
            # 也就是,它自己的第8个父节点 + 该父节点的第2个父节点 = 该节点的第10个父节点
            if k & (1 << i):
                node = self.dp[node][i]
                if node == -1:
                    break
        return node


if __name__ == "__main__":
    test = []
