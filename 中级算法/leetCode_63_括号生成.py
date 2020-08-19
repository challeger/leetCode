"""
day: 2020-08-19
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xv33m7/
题目名: 括号生成
题目描述: 数字n代表生成括号的对数,请你设计一个函数,用于能够生成所有可能的并且有效的括号组合
示例:
    输入: n=3
    输出: [
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
思路:
1. 回溯法
    当目前左括号数大于等于右括号数时,那么目前的 括号字符串必然 可以成为一个有效字符串
    所以我们设定,left=剩余的左括号数,right=剩余的右括号数
    当left==right时,只能添加左括号,
    否则当left<right时,可以添加左括号,也可以添加右括号
    当left==0 and right == 0时,当前的字符串就是一个有效的括号组合
2. 动态规划
    对于n对括号组成的有效括号字符串,它要组成新的括号字符串,
    必然是 '(' + n-1对括号中的任意对括号 + ')' + n-1对括号中剩余的括号对
    所以我们的核心算法大概是
    for i in range():
        for j in range(i-1):
            # 新括号内的括号对
            left = dp[j]
            # 新括号外的括号对
            right = dp[i-j-1]
            for s1 in left:
                for s2 in right:
                    '(' + s1 + ')' + s2
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # def backtrack(combination, left, right):
        #     if not left and not right:
        #         res.append(combination)
        #     elif left == right:
        #         backtrack(combination + '(', left-1, right)
        #     elif left < right:
        #         if left:
        #             backtrack(combination + '(', left-1, right)
        #         if right:
        #             backtrack(combination + ')', left, right-1)
        # res = []
        # if n:
        #     backtrack('', n, n)

        # 动态规划
        if not n:
            return []
        dp = [None for _ in range(n+1)]
        dp[0] = ['']
        for i in range(1, n+1):
            cur = []
            for j in range(i):
                # 新括号内的括号对
                left = dp[j]
                # 新括号外的括号对
                right = dp[i-j-1]
                for s1 in left:
                    for s2 in right:
                        cur.append('('+s1+')'+s2)
            dp[i] = cur
        return dp[n]


if __name__ == "__main__":
    test = 3
    s = Solution()
    print(s.generateParenthesis(test))
