"""
day: 2020-08-30
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xd2egr/
题目名: 正则表达式匹配
给你一个字符串s和一个字符规律p,请你来实现一个支持'.'和'*'的正则表达式匹配
    '.': 匹配任意单个字符
    '*': 匹配0个或多个前面的那一个元素
示例:
    输入: s='aa', p='a'
    输出: false
    输入: s='aa', p='a*'
    输出: true
    输入: s='ab', p='.*'
    输出: true
    输入: s='aab', p='c*a*b'
    输出: true
思路:
1. 动态规划
    对于s的前i个字符与p的前j个字符,它们之间只会有两种情况:
        1. 匹配 -> true
        2. 不匹配->false
    对于p的第j个字符,dp[i][j]的状态应该为:
        当p是小写字符时,当s[i] == p[j]时, dp[i][j] = dp[i-1][j-1]
        否则为false.
        当p是*时,对于星号,我们可以选择不使用它(匹配0个字符),或使用它(匹配1到n个字符)
        当我们不使用它时,那么dp[i][j]的状态应该是对应前两个格子的状态(也就是*前面的一个字符也不进行匹配),dp[i][j-2]
        当我们使用它时,就需要判断前面一个字符与当前字符是否相等,相等的话就是dp[i-1][j],否则就是false
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def charMatch(s_idx, p_idx):
            if s_idx == 0:
                return False
            if p[p_idx-1] == '.':
                return True
            return s[s_idx-1] == p[p_idx-1]

        m = len(s)
        n = len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        # 两个字符串为空时,必定匹配
        dp[0][0] = True
        for i in range(m+1):
            for j in range(1, n+1):
                if charMatch(i, j):
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = (charMatch(i, j-1) and dp[i-1][j]) or dp[i][j-2]
        return dp[m][n]


if __name__ == "__main__":
    s_test = ''
    p_test = '.*'
    s = Solution()
    print(s.isMatch(s_test, p_test))
