"""
day: 2020-08-28
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xdxc56/
题目名: 朋友圈
班上有N名学生.其中有些人是朋友,有些则不是.他们的友谊具有传递性.如果已知A是B的朋友,B是C的朋友,那么我们可以认为
A也是C的朋友,所谓朋友圈,是指所有朋友的集合
给定一个N*N的矩阵M,表示班级中学生之间的朋友关系,如果M[i][j] = 1,表示已知第i个和j个学生互为朋友关系,否则为不知道,你
必须输出所有学生中的已知的朋友圈总数
示例:
    输入:
    [
        [1,1,0],
        [1,1,0],
        [0,0,1]
    ]
    输出: 2
思路:
1. 深度优先搜索
    定义一个数组visited, visited[i]表示第i个学生是否被访问过
    访问每一个学生,若在访问这个学生时,这个学生还未被访问过,那么说明
    遇到了一个新的朋友圈..那么我们继续深度遍历这个学生的所有相邻节点,
    一直遍历到没有相邻节点访问,回溯到之前的节点,进行下一次访问
2. 广度优先搜索
    我们从一个节点开始,访问它所有邻接的节点,然后对于这些节点,我们继续访问他们的邻接节点.
    直到访问了所有可以到达的节点..
3. 并查集
    将所有是朋友的节点连接起来,最终有几个连接块就有几个朋友圈.
"""
from typing import List


class UnionFind:
    def __init__(self, n):
        super().__init__()
        self.count = n
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def get_count(self):
        return self.count

    def find(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        # 如果已经连通就直接返回
        if p_root == q_root:
            return

        # 高度较小的树,添加到高度较大的树上
        if self.rank[p_root] > self.rank[q_root]:
            self.parent[q_root] = p_root
        elif self.rank[p_root] < self.rank[q_root]:
            self.parent[p_root] = q_root
        # 若高度一样,则添加之后,高度要+1
        else:
            self.parent[q_root] = p_root
            self.rank[p_root] += 1
        # 每归并一次,不同的连通快的count就-1
        self.count -= 1


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # 深度优先
        # def dfs(i):
        #     for idx in range(m):
        #         if M[i][idx] and not visited[idx]:
        #             visited[idx] = 1
        #             dfs(idx)
        # m = len(M)
        # if not m:
        #     return 0
        # count = 0
        # visited = [0] * m
        # for i in range(m):
        #     if not visited[i]:
        #         count += 1
        #         dfs(i)
        # return count

        # 广度优先
        # m = len(M)
        # if not m:
        #     return 0
        # count = 0
        # visited = [0] * m
        # from collections import deque
        # queue = deque()
        # for i in range(m):
        #     if not visited[i]:
        #         queue.append(i)
        #         while queue:
        #             s = queue.popleft()
        #             visited[s] = 1
        #             for j in range(m):
        #                 if M[s][j] and not visited[j]:
        #                     queue.append(j)
        #         count += 1
        # return count

        # 并查集
        m = len(M)
        if not m:
            return 0
        uf = UnionFind(m)
        for i in range(m):
            # 因为是对称矩阵,所以只需要遍历一般就行.
            for j in range(i+1, m):
                if M[i][j]:
                    uf.union(i, j)
        return uf.count


if __name__ == "__main__":
    test = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]]
    s = Solution()
    print(s.findCircleNum(test))
