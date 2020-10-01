"""
day: 2020-10-01
url: https://leetcode-cn.com/problems/UlBDOe/
题目名: 秋叶收藏集
小扣出去秋游,途中收集了一些红叶和黄叶,他利用这些叶子初步整理了一份秋叶收藏集 leaves
字符串 leaves 仅包含小写字符 r 和 y, 其中字符 r 表示一片红叶,字符 y 表示一片黄叶.
出于美观整齐的考虑,小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分.
每部分树叶数量可以不相等,但均需大于等于 1.
每次调整操作,小扣可以将一片红叶替换成黄叶或者将一片黄叶替换成红叶.
请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕
思路:
    动态规划:
        对于替换完成的叶子序列,每一片叶子只可能出现三种状态:
        1. 左边的r叶子  -> 该叶子的左边叶子是状态1
        2. 中间的y叶子  -> 该叶子的左边叶子是状态1或者状态2
        3. 右边的r叶子  -> 该叶子的左边叶子是状态2或者状态3
        那么就可以写出dp的状态转移方程
        dp[i][0] = dp[i-1][0] + isYellow(i)  后面一个表示当前叶子的颜色,如果是r则不需要+1
        dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + isRed(i)  当前叶子是y叶子则不需要+1
        dp[i][2] = min(dp[i-1][1], dp[i-1][2]) + isYellow(i)
        最终dp[-1][2]就是我们的答案
"""


class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        dp = [[0, 0, 0] for _ in range(n)]
        dp[0][0] = int(leaves[0] == 'y')
        dp[0][1] = dp[0][2] = float('inf')
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + int(leaves[i] == 'y')
            dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + int(leaves[i] == 'r')
            dp[i][2] = min(dp[i-1][1], dp[i-1][2]) + int(leaves[i] == 'y')
        return dp[-1][2]
