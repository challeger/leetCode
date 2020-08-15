"""
day: 2020-08-15
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnsdi2/
题目名: 3的幂
题目描述: 给定一个整数,写一个函数来判断它是否是3的幂次方
示例:
    输入: 27
    输出: true
    输入: 0
    输出: false
    输入: 45
    输出: false
思路:
对数公式
    设3^x = n
    x = ln(n) / ln(3),然后判断x是不是整数即可
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # return n > 0 and 1162261467 % n == 0
        if n <= 0:
            return False
        import math
        origin = math.log(n) / math.log(3)
        eps = 1e-10
        return abs(origin - round(origin)) < eps


if __name__ == "__main__":
    sl = Solution()
    print(sl.isPowerOfThree(9))
    print(sl.isPowerOfThree(10))
    print(sl.isPowerOfThree(100))
    print(sl.isPowerOfThree(243))
