"""
day: 2020-08-15
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn1m0i/
题目名: 位1的个数
题目描述: 输入是一个无符号整数,返回其二进制表达式中数字位数为1的个数
示例:
    输入: 00000000000000000000000000001011
    输出: 3
    输入: 11111111111111111111111111111101
    输出: 32
思路:
    每次将最右边的数字与1进行与运算,然后将n右移一位
    直到n=0
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
        # foo = n
        # count = 0
        # while foo:
        #     count += foo & 1
        #     foo = foo >> 1
        # return count
