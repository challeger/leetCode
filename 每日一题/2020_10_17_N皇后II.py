"""
day: 2020-10-17
url: https://leetcode-cn.com/problems/n-queens-ii/
题目名: N皇后II
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上,并且使皇后彼此之间不能相互攻击

给定一个整数 n，返回 n 皇后不同的解决方案的数量
思路:
位运算:
    首先因为一列上只能有一个皇后,所以可以用位运算来判断是否可以放皇后
    在当前格子放上皇后后, 那么 这一列, 这格子的左对角线, 这一列的右对角线都不能放皇后
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        target = (1 << n) - 1  # 全为1

        def dfs(row, col, left, right):
            # col表示哪些位置已经放了皇后了
            # left表示从左下到右上的对角线,
            # right表示从左上到右下的对角线
            nonlocal count
            if row >= n:  # 如果等于,说明所有行都摆好了
                count += 1
                return
            bit = ~(col | left | right) & target  # 将所有空位标记为1,非空位标记为0
            while bit > 0:
                choice = bit & -bit  # 获取最后一位高位
                # 下一行的占位直接 | 上当前选择的位即可
                # 下一行的left对角线在 | 上当前选择的位后,应该整体左移一位
                # 下一行的right对角线在 | 上当前选择的位后,应该整体右移一位
                dfs(row+1, col | choice, (left | choice) << 1, (right | choice) >> 1)
                bit &= bit - 1  # 去掉最后一位1

        dfs(0, 0, 0, 0)
        return count

    def totalNQueens_1(self, n: int) -> int:
        def backtrack(row):
            if row == n:
                return 1
            count = 0
            for i in range(n):
                if i in col or row - i in left or row + i in right:
                    continue
                col.add(i)
                left.add(row - i)
                right.add(row + i)
                count += backtrack(row + 1)
                col.remove(i)
                left.remove(row - i)
                right.remove(row + i)
            return count
        col = set()
        left = set()
        right = set()
        return backtrack(0)


if __name__ == "__main__":
    s = Solution()
    print(s.totalNQueens_1(4))
