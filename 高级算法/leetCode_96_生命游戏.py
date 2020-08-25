"""
day: 2020-08-25
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xwk53e/
题目名: 生命游戏
题目描述: 给定一个包含m x n个格子的面板,每一个格子都可以看成是一个细胞.每个细胞都具有一个初始状态: 1即为活细胞,0即为死细胞
每个细胞与其八个相邻位置(水平,垂直,对角线)的细胞都遵循以下四条生存定律:
    1. 如果活细胞周围八个位置的活细胞少于两个,则该位置活细胞死亡
    2. 如果活细胞周围八个位置有两个或三个活细胞,则该位置活细胞仍然存活
    3. 如果活细胞周围八个位置有超过三个活细胞,则该位置活细胞死亡
    4. 如果死细胞周围正好有三个活细胞,则该位置死细胞复活
根据当前状态,写一个函数来计算面板上所有细胞的下一个状态.下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的,其中细胞的
出生与死亡是同时发生的
示例:
    输入： 
    [
      [0,1,0],
      [0,0,1],
      [1,1,1],
      [0,0,0]
    ]
    输出：
    [
      [0,0,0],
      [1,0,1],
      [0,1,1],
      [0,1,0]
    ]
思路:
1. 利用额外空间记录上一行的原本的状态,与左边元素的原本的状态

2. 额外状态
    我们用个位来表示当前细胞的状态,用十位来表示这个细胞周围的活细胞数量
    第一次遍历记录活细胞数量,第二次遍历修改状态.
"""
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # rows = len(board)
        # if rows:
        #     columns = len(board[0])
        #     directions = [(0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1), (1, 1), (1, 0), (1, -1)]
        #     line = [0] * columns
        #     left_cell = 0
        #     for row in range(rows):
        #         temp = board[row][:]
        #         for column in range(columns):
        #             count = 0
        #             temp_left = board[row][column]
        #             for direction in directions:
        #                 new_row, new_column = row + direction[0], column + direction[1]
        #                 if 0 <= new_row < rows and 0 <= new_column < columns:
        #                     if direction[0] == -1:
        #                         count += line[new_column]
        #                     elif direction[0] == 0 and direction[1] == -1:
        #                         count += left_cell
        #                     else:
        #                         count += board[new_row][new_column]
        #             if count < 2 or count > 3:
        #                 board[row][column] = 0
        #             elif board[row][column] == 0 and count == 3:
        #                 board[row][column] = 1
        #             left_cell = temp_left
        #         line = temp
        m = len(board)
        n = len(board[0])

        # 如果当前格子是活细胞
        # 那么就把这个格子周围八个格子的值+10
        def record(x, y):
            for i in (x-1, x, x+1):
                for j in (y-1, y, y+1):
                    if x == i and y == j:
                        continue
                    if 0 <= i < m and 0 <= j < n:
                        board[i][j] += 10

        # 根据当前格子周围的活细胞数量
        # 来进行状态更改
        def update(x, y):
            value = board[x][y]
            if value // 10 == 3:
                board[x][y] = 1
            elif value // 10 == 2 and value % 10 == 0:
                board[x][y] = 1
            else:
                board[x][y] = 0

        for i in range(m):
            for j in range(n):
                if board[i][j] % 10:
                    record(i, j)

        for i in range(m):
            for j in range(n):
                update(i, j)


if __name__ == "__main__":
    test = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    s = Solution()
    s.gameOfLife(test)
    print(test)
