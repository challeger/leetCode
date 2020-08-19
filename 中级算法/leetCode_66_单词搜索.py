"""
day: 2020-08-19
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvkwe2/
题目名: 单词搜索
题目描述: 给定一个二维网格和一个单词,找出该单词是否存在与网格中.
单词必须按照字母顺序,通过相邻的单元格内的字母构成,其中'相邻'单元格是那些水平相邻或垂直相邻的单元格,
同一个单元格内的字母不允许被重复使用
示例:
    board =
    [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
    ]

    给定 word = "ABCCED", 返回 true
    给定 word = "SEE", 返回 true
    给定 word = "ABCB", 返回 false
思路:
    找第一位字母时,需要找自身,
    找下一位字母时,需要从上下左右四个方向找,并防止越界
    一旦找到需要的字母,就将那位字母标记为已使用,然后移动到那位字母上,并将要查找的字符后移一位进行下一次查找
    查找完成后,将字母重新设置为原来的值,也就是状态回溯,直到没有要查找的数字了,或者board遍历完了.
"""
from typing import List


class Solution:
    directions = [(0, 0), (-1, 0), (0, -1), (1, 0), (0, 1)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(x, y, trace_str):
            if not trace_str:
                return True
            for direction in (self.directions[1:] if len(trace_str) != len(word) else self.directions[:1]):
                new_x, new_y = x + direction[0], y + direction[1]
                if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] == trace_str[0]:
                    # 将该格标记为已使用
                    board[new_x][new_y] = 1
                    if backtrack(new_x, new_y, trace_str[1:]):
                        return True
                    # 状态回溯
                    board[new_x][new_y] = trace_str[0]
        m = len(board)
        if not m or not word:
            return False
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, word):
                    return True
        return False


if __name__ == "__main__":
    test = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = 'ABCCED'
    s = Solution()
    print(s.exist(test, word))
