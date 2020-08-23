"""
day: 2020-08-23
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xwrzwc/
题目名: x的平方根
题目描述: 实现int sqrt(int x)函数
结果只保留整数的部分
示例:
    输入: 4
    输出: 2
    输入: 8
    输出: 2
思路:
1. 二分查找
    找到第一个平方大于x的数,返回前一个数即可.
2. 牛顿迭代
    对于方程f(x) = x^2-C
    当C是我们要求平方根的数时,那么x的零点就是C的正负平方根
    y = 0.5(x + C/x)
    当y与x足够小时,可以认为当前的x与零点已经非常近了,因为我们只要整数
    所以可以直接Int(x)
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        # left, right, res = 0, x, -1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if mid * mid <= x:
        #         res = mid
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        if not x:
            return 0
        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi
        return int(x0)


if __name__ == "__main__":
    test = 10
    s = Solution()
    print(s.mySqrt(test))
