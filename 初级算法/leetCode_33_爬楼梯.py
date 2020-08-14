"""
day: 2020-08-14
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn854d/
题目名: 爬楼梯
题目描述: 假设你正在爬楼梯,需要n阶你才能到达楼顶,每次你可以爬1或2个台阶,你有多少种不同的方法可以爬到楼顶呢?
示例:
    输入: 2
    输出: 2
    1.  1 + 1
    2. 2
    输入: 3
    输出: 3
    1. 1 + 1 + 1
    2. 1 + 2
    3. 2 + 1
思路:
1. 动态规划
    用f(x)来表示爬到第x阶台阶的方案数,最后一步我们可能跨1,也可能跨2,所以
    f(x) = f(x-1) + f(x-2)
    将f(0)设置为0,也就是从第0阶爬到第0阶只有一种方案,从第0阶爬到第1阶也只有一种方案
    f(1)=1, 所以我们只要设置循环, p=f(x-1), q=f(x-2), r=f(x),每次循环让p=q,q=r,r=p+q即可
    最终返回r
2. 斐波那契数列
    爬楼梯的数列本质就是斐波那契数列,所以可以通过斐波那契数列的公式直接求解
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        p, q, r = 1, 2, 0
        for _ in range(2, n):
            r = p + q
            p = q
            q = r
        return max(n, r)

        # import math
        # sqrt5 = 5 ** 0.5
        # fibin = math.pow((1+sqrt5)/2, n+1)-math.pow((1-sqrt5)/2, n+1)
        # return int(fibin/sqrt5)


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(3))
