"""
day: 2020-08-24
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xwaiag/
题目名: 两整数之和
题目描述: 不使用运算符+和-,计算两整数a,b之和
示例:
    输入: a=1, b=2
    输出:3
思路:
    无符号的加法 -> a ^ b
    求进位 -> (a & b)  << 1
    当结果>=0x80000000时(32位负数的开始),对它取反,计算机会将它转换为补码, 补码会将除符号位以外的
    位取反,然后+1 
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 转为32位无符号整数
        a = a & 0xffffffff
        b = b & 0xffffffff
        while b:
            # 进位
            carry = a & b
            # 无进位加法
            a ^= b
            # 把进位给左移一位,后面是模拟溢出
            b = (carry << 1) & 0xffffffff
        # int的值域是[-2^31, 2^31-1]
        # 当a>=0x80000000时,说明它是一个负数
        # 那么我们将a与0xffffffff异或,然后取反就得到了
        # 异或是恢复原来的位数,取反之后会根据第一位符号位转换为补码.
        return a if a < 0x80000000 else ~(a ^ 0xffffffff)


if __name__ == "__main__":
    test1 = -2
    test2 = 0
    s = Solution()
    print(s.getSum(test1, test2))
