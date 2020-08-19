"""
day: 2020-08-18
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvtsnm/
题目名: 岛屿数量
题目描述: 给你一个由'1'(陆地)和'0'(水)组成的二维网格,请你计算网格中岛屿的数量
岛屿总是被水包围,并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成.
此外,该网格的四条边均被水包围.
示例:
    输入:
        [
        ['1','1','1','1','0'],
        ['1','1','0','1','0'],
        ['1','1','0','0','0'],
        ['0','0','0','0','0']
        ]
    输出: 1
    输入:
        [
        ['1','1','0','0','0'],
        ['1','1','0','0','0'],
        ['0','0','1','0','0'],
        ['0','0','0','1','1']
        ]
    输出: 3
思路:
1. 深度优先
    每当我们发现一块没有遍历过的陆地,就将这块陆地连通的所有陆地都标记为已遍历过,这样视为
    发现了一片岛屿.
    标记的方法是:将当前所在的陆地按照(上,左,右,下)的顺序移动,若某个方向的格子是一片未标记的陆地
    就移动到该格子上并标记,然后继续移动.
2. 广度优先
    定义一个辅助栈来存放下一个要去的陆地格子,每次找到新的陆地就将它标记为已遍历,然后找下一个格子
    直到全部找完.
3. 并查集
    将连通的格子全部链接起来,最终有几个连接块就说明有几块大陆.
    并查集主要有三个操作:
    1.find: 查找元素的根节点
    2.isConnected: 判断两个元素是否链接,即根节点是否相等
    3.union: 将两个元素连接起来(先找到它们的根节点,然后让其中一个根节点指向另一个根节点)
    并查集初始化时,不相连的大陆count应该是矩阵的长度,每执行一次连接操作,count-=1
"""
from typing import List
from collections import deque


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
        if p_root == q_root:
            return

        if self.rank[p_root] > self.rank[q_root]:
            self.parent[q_root] = p_root
        elif self.rank[p_root] < self.rank[q_root]:
            self.parent[p_root] = q_root
        else:
            self.parent[q_root] = p_root
            self.rank[p_root] += 1
        self.count -= 1


class Solution:
    # 方向数组,代表相对于当前位置的4个方向的横纵坐标的偏移量
    # directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    # def dfs(self, grid, i, j, m, n, marked):
    #     # 将当前格子标记为访问过
    #     marked[i][j] = True
    #     # 这个操作会将当前陆地格子连通的所有陆地格子都标记为访问过.
    #     for direction in self.directions:
    #         new_i = i + direction[0]
    #         new_j = j + direction[1]
    #         if -1 < new_i < m and -1 < new_j < n and not marked[new_i][new_j] and grid[i][j] == '1':
    #             self.dfs(grid, new_i, new_j, m, n, marked)

    def numIslands(self, grid: List[List[str]]) -> int:
        # m = len(grid)
        # if not m:
        #     return 0
        # n = len(grid[0])
        # # 用于判断对应的格子是否被访问过
        # marked = [[False for _ in range(n)] for _ in range(m)]
        # count = 0
        # for i in range(m):
        #     for j in range(n):
        #         # 如果没有访问过且是陆地,说明发现了一片新的陆地
        #         if not marked[i][j] and grid[i][j] == '1':
        #             count += 1
        #             self.dfs(grid, i, j, m, n, marked)
        # return count

        # 广度优先算法
        # m = len(grid)
        # if not m:
        #     return 0
        # n = len(grid[0])
        # count = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == '1':
        #             count += 1
        #             grid[i][j] = '0'
        #             neighbors = deque([(i, j)])
        #             while neighbors:
        #                 x, y = neighbors.popleft()
        #                 for direction in self.directions:
        #                     new_i, new_j = x + direction[0], y + direction[1]
        #                     if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == '1':
        #                         neighbors.append((new_i, new_j))
        #                         grid[new_i][new_j] = '0'
        # return count

        # 并查集
        row = len(grid)
        if not row:
            return 0
        col = len(grid[0])

        def get_index(x, y):
            return x * col + y

        directions = [(1, 0), (0, 1)]
        # 定义一个虚拟节点,用来将所有的水相连
        dummy_node = row * col
        uf = UnionFind(dummy_node + 1)
        for i in range(row):
            for j in range(col):
                # 如果是水,就与虚拟节点连接起来
                if grid[i][j] == '0':
                    uf.union(get_index(i, j), dummy_node)
                # 如果是大陆,则尝试与下方和右方的格子相连
                if grid[i][j] == '1':
                    for direction in directions:
                        new_i = i + direction[0]
                        new_j = j + direction[1]
                        if new_i < row and new_j < col and grid[new_i][new_j] == '1':
                            uf.union(get_index(i, j), get_index(new_i, new_j))
        # 最终返回的结果要减去水的相连部分
        return uf.get_count() - 1


if __name__ == "__main__":
    test = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    s = Solution()
    print(s.numIslands(test))
