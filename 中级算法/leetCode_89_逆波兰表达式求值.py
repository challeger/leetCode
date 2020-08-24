"""
day: 2020-08-24
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xw20mv/
题目名: 逆波兰表达式求值
题目描述: 根据 逆波兰表示法，求表达式的值。
有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
示例:
    输入: ["2", "1", "+", "3", "*"] (2+1)*3
    输出: 9
思路:
    如果小数部分有循环,那么循环开始时的余数必然在之前出现过一次
    以此为依据来判断是否进入了循环.
"""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        stack = []
        hashmap = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
        }
        for char in tokens:
            if char in hashmap.keys():
                b = stack.pop()
                stack[-1] = int(hashmap[char](stack[-1], b))
            else:
                stack.append(int(char))
        return stack[0]


if __name__ == "__main__":
    test = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    s = Solution()
    print(s.evalRPN(test))
