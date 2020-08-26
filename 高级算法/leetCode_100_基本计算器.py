"""
day: 2020-08-25
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xwsg7t/
题目名: 基本计算器II
实现一个基本的计算器来计算一个简单的字符串表达式的值
表达式仅包含非负整数 +,-,*,/ 四种运算符和空格 .整数除法仅保留整数部分
示例:
    输入: '3+2*2'
    输出: 7
    输入: ' 3/2 '
    输出: 1
    输入: ' 3+5 / 2 '
思路:
    利用栈,遇到+号,就把+后面的数字推入栈中,-号,将-num推入栈中
    *号,将栈顶元素与num相乘,/号,将栈顶元素与num相除
    最后对栈中元素求和.
"""


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in '+-*/' or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] *= num
                else:
                    stack[-1] = int(stack[-1] / num)
                num = 0
                sign = s[i]
        return sum(stack)


if __name__ == "__main__":
    test = '14-3/2'
    s = Solution()
    print(s.calculate(test))
