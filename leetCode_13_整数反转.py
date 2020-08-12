"""
day: 2020-08-12
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnx13t/
题目名: 整数反转
题目描述: 给出一个32位的有符号整数,需要将这个整数中每位上的数字进行反转
示例:
    输入: 123
    输出: 321
思路:
1. 类型转换
    转为字符串->反转->转为整型,转整型时需要对正负进行一些处理
2. 整除与取余
    每次循环对x%10,得到最低位数pop,然后将result*10+pop,这样就进行了反转
    每次循环计算前判断是否会溢出
"""


class Solution(object):
    @staticmethod
    def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        # result = int(str(x)[::-1]) if x >= 0 else int('-' + str(x)[::-1][:-1])
        # return result if result in range(-2**31, 2**31) else 0

        INT_MAX = (1 << 31) - 1
        sign = (x >= 0)
        x = abs(x)
        result = 0
        while x != 0:
            pop = x % 10
            x //= 10
            if (result > INT_MAX/10) or (result == (INT_MAX / 10) and pop > 7):
                return 0
            result = result * 10 + pop
        return result if sign else -result


if __name__ == "__main__":
    test = -123
    print(Solution.reverse(test))
