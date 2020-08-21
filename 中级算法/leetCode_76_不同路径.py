"""
day: 2020-08-21
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvjigd/
题目名: 不同路径
题目描述: 一个机器人位于一个m x n网格的左上角,机器人每次只能向下或者右移动一步,
机器人试图达到网格的右下角,问总共有多少条不同的路径
示例:
    输入: m=3, n=2
    输出: 3
思路:
因为只能向右或者向下走,所以到达(x,y)的方法就是到达(x,y)上方的方法+到达(x, y)左方的方法
    dp[x][y] = dp[x-1][y] + dp[x][y-1]
因为我们是一列一列扫描的,所以只需要定义一个长度为n的数组dp,记录上一列的走的方法,然后在我们遍历这一行时
当前dp[i]就是上方的方法,dp[i-1]就是左方的方法.
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0
        dp = [1] * n
        for x in range(1, m):
            for y in range(1, n):
                dp[y] += dp[y-1]
        return dp[-1]


if __name__ == "__main__":
    test1 = 7
    test2 = 3
    s = Solution()
    print(s.uniquePaths(test1, test2))
