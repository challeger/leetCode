"""
day: 2020-08-27
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xwfor1/
题目名: 被围绕的区域
给定一个二维的矩阵,包含'X'和'O'
找到所有被'X'围绕的区域,并将这些区域里所有的'O'用'X'填充.

被围绕的区间不会存在于边界上,如果两个元素在水平或垂直方向相邻,那么它们是相邻的
示例:
    输入:
    X X X X
    X O O X
    X X O X
    X O X X
    输出:
    X X X X
    X X X X
    X X X X
    X O X X
思路:
1. 核心: 标记法
    我们将所有与边界O相连的内部O标记为A,然后遍历数组,如果是A则替换为O,如果是O则替换为X
2. 标记算法:DFS
    深度优先遍历,直接递归的从顶部,底部,左侧,右侧来深度遍历,将所有与边界O相连的O都标记为A
    然后根据标记替换
3. BFS
    广度优先遍历,先将所有的边界O的坐标加入队列中,然后依次弹出队首,将该处标记为'A'
    并将队首周围的'O'的坐标加入队列中,直到队列为空.然后根据标记替换
"""
from typing import List


class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        def dfs(x, y):
            if not 0 <= x < m or not 0 <= y < n or board[x][y] != 'O':
                return
            board[x][y] = 'A'
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        m = len(board)
        n = len(board[0])

        # # 找边界上的'O',然后递归找与它相邻的为'O'的元素,标记为'A'
        # for i in range(m):
        #     dfs(i, 0)
        #     dfs(i, n-1)
        # for i in range(n-1):
        #     dfs(0, i)
        #     dfs(m-1, i)
        # for i in range(m):
        #     for j in range(n):
        #         # 被标记了'A'的就是与边界'O'相邻的'O'
        #         if board[i][j] == 'A':
        #             board[i][j] = 'O'
        #         # 否则是不相邻的'O'
        #         elif board[i][j] == 'O':
        #             board[i][j] = 'X'

        from collections import deque
        queue = deque()
        for i in range(m):
            if board[i][0] == 'O':
                queue.append((i, 0))
            if board[i][n-1] == 'O':
                queue.append((i, n-1))
        for i in range(n):
            if board[0][i] == 'O':
                queue.append((0, i))
            if board[m-1][i] == 'O':
                queue.append((m-1, i))
        while queue:
            x, y = queue.popleft()
            board[x][y] = 'A'
            for direction in self.directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] == 'O':
                    queue.append((new_x, new_y))
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


if __name__ == "__main__":
    test = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
            ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    s = Solution()
    s.solve(test)
    print(test)
