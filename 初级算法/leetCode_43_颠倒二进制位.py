"""
day: 2020-08-15
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn1m0i/
题目名: 颠倒二进制位
题目描述: 颠倒给定的 32 位无符号整数的二进制位
示例:
    输入: 00000010100101000001111010011100
    输出: 00111001011110000010100101000000
    输入: 11111111111111111111111111111101
    输出: 10111111111111111111111111111111
思路:
1. 设输入的数字为n,结果为res,每次让n的最后一位左移31-i位,加到res上
然后将n右移一位

2.  将32位分成两个16位,互换位置
    将16位分成两个8 位,互换位置
    将8 位分成两个4 位,互换位置
    将4 位分成两个2 位,互换位置
    将2 位分成两个1 位,互换位置
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        # res, power = 0, 31
        # while n:
        #     res += (n & 1) << power
        #     n = n >> 1
        #     power -= 1
        # return res
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n
