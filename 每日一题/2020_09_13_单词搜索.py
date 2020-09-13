"""
day: 2020-09-13
url: https://leetcode-cn.com/problems/word-search/
题目名: 单词搜索
给定一个二维网格和一个单词,找出该单词是否存在于网格中.

单词必须按照字母顺序,通过相邻的单元格内的字母构成,其中“相邻”单元格是那些水平相邻或垂直相邻的单元格.
同一个单元格内的字母不允许被重复使用.
思路:
    dfs + 回溯
"""
from typing import List


class Solution:
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if not m or not word:
            return False
        n = len(board[0])

        def backtrack(x, y, path):
            if not path:
                return True
            for direction in self.directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] == path[0]:
                    board[new_x][new_y] = 1  # 标记为已使用
                    if backtrack(new_x, new_y, path[1:]):
                        return True
                    board[new_x][new_y] = path[0]  # 回溯
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    board[i][j] = 1
                    if backtrack(i, j, word[1:]):
                        return True
                    board[i][j] = word[0]
        return False
