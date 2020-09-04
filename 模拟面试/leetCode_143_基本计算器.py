"""
day: 2020-09-04
url: https://leetcode-cn.com/problems/basic-calculator/
题目名: 基本计算器
实现一个基本的计算器来计算一个简单的字符串表达式的值
字符串表达式可以包括左括号(, 右括号), 加号+, 减号-,非负整数和空格
示例:
    输入: "(1+(4+5+2)-3)+(6+8)"
    输出: 23
思路:
 利用数字的正负号来代替 + - 操作,这样只需要执行加法即可,
 对于一个3位的数字123,他会占用3个字符,所以我们在获取数字时,需要一个值operand来记录当前数字
 的累计值,每次都将operand*10 + int(ch),直到遇到其他符号,
 当我们遇到 +-号时,根据之前标记的符号位sign, 来决定是加正数还是加负数;
 然后清空operand,并根据当前的+-号,设置符号位
 当我们遇到(号时,需要将(前算出的结果,与(前一位符号位推入栈中,然后将所有值清空,计算括号中的值,
 直到遇到一个),我们就将当前计算出的括号中的值,与栈中的符号位相乘,然后再与栈中的结果相加..
 以此类推,直到最后计算完成,因为有可能是数字结尾,所以我们还需要在最后 + sign*operand
"""


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        res = 0
        sign = 1
        for ch in s:
            # 如果是数字,继续找下一个数字,直到将该数字全部找到
            if ch.isdigit():
                operand = (operand * 10) + int(ch)
            # 根据上一位的符号位来决定是 正数还是负数
            # 并根据当前符号位来设置符号位
            elif ch == '+':
                res += sign * operand
                sign = 1
                operand = 0
            elif ch == '-':
                res += sign * operand
                sign = -1
                operand = 0
            # 如果是左括号,先将之前计算出的结果与括号前一个符号位推入栈中
            # 然后继续计算括号中的值
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            # 遇到右括号,说明当前括号里的值计算完成
            # 先将括号里的值与左括号前的符号进行相乘,然后与左括号前计算出的值相加
            elif ch == ')':
                # 符号位
                res *= stack.pop()
                # 数字位
                res += stack.pop()
                operand = 0
        # 可能会出现以数字结尾的情况.
        return res + sign * operand
