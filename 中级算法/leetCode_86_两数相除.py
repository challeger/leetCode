"""
day: 2020-08-23
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xwp6vi/
题目名: 两数相除
题目描述: 给定两个整数,被除数dividend和除数divisor.将两数相除,要求不使用乘法,除法和mod运算符.
返回被除数dividend除以除数divisor得到的商
得到的结果只要整数部分
示例:
    输入: dividend = 10, divisor = 3
    输出: 3
    输入: dividend = 7, divisor = -3
    输出: -2
思路:
    每次都让divisor翻倍,直到下次翻倍会超过dividend
    则记录下count,然后去计算dividend-当前的divisor,除divisor的count
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def div(n1, n2):
            # 因为只要整数部分,所以被除数大于除数时直接返回0
            if n1 < n2:
                return 0
            # 记录用了多少个n2
            count = 1
            # 记录count个n2的总和
            n2_plus = n2
            while n2_plus <= n1-n2_plus:
                # 使用次数翻倍
                count += count
                # 总和翻倍
                n2_plus += n2_plus
            # 计算剩余的被除数中,需要用到多少个n2
            return count + div(n1-n2_plus, n2)

        # 越界与特判处理
        if not dividend or divisor == 1:
            return dividend
        if divisor == -1:
            return -dividend if dividend > (-1 << 31) else (1 << 31)-1
        # 正负判断
        sign = (dividend > 0) ^ (divisor > 0)
        num1 = abs(dividend)
        num2 = abs(divisor)
        res = div(num1, num2)
        return -res if sign else res


if __name__ == "__main__":
    test1 = 4
    test2 = 3
    s = Solution()
    print(s.divide(test1, test2))
