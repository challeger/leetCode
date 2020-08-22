"""
day: 2020-08-22
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xwehi5/
题目名: 阶乘后的零
题目描述: 给定一个整数n,返回n!结果尾数中的零的数量
示例:
    输入: 3
    输出: 3!=6, return 0
    输入: 5
    输出: 5!=120, return 1
思路:
    有多少个5就有多少个0,所以每次将n除5,然后count加上得到的数
    直到n等于0
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero_count = 0
        while n > 0:
            n //= 5
            zero_count += n
        return zero_count
