"""
day: 2020-09-15
url: https://leetcode-cn.com/problems/sudoku-solver/
题目名: 解数独
编写一个程序,通过已填充的空格来解决数独问题

思路:
    用回溯法, 用三个列表来记录每个数字在每一行,每一列,每一个3x3的格子中是否能够被填写.
    然后先遍历一遍数组,将这三个列表的值确定好,并将所有空格也加入一个列表中.
    之后遍历空格,判断1-9中是否有数字可以填入这个空格中,如果可以填入就尝试填入,并将对应的格子标记为False,意为已经填入
    直到某次不能填入,那么就结束本次dfs,回溯到上一次的状态,将对应格子标记为True
    直到填满了所有的空格,那么说明该数独已经解出来了.
"""
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 表示元素是否可以填在第i行
        line = [[True] * 9 for _ in range(9)]
        # 表示元素是否可以填在第i列
        column = [[True] * 9 for _ in range(9)]
        # 表示元素是否可以填在这个3x3的矩阵中
        block = [[[True] * 9 for i in range(3)] for j in range(3)]
        # 表示是否已经将数独全部填满了
        valid = False
        # 空格列表
        spaces = []

        def dfs(pos):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return
            i, j = spaces[pos]
            for digit in range(9):
                if all((line[i][digit], column[j][digit], block[i // 3][j // 3][digit])):
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = False
                    board[i][j] = str(digit + 1)
                    dfs(pos + 1)
                    # 回溯
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True
                if valid:
                    return

        for i in range(9):
            for j in range(9):
                # 如果是空格,就加入空格列表中
                if board[i][j] == '.':
                    spaces.append((i, j))
                # 否则就将该位置的数字标记为已经存在.
                else:
                    digit = int(board[i][j]) - 1
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = False
        dfs(0)
