"""
day: 2020-09-07
url: https://leetcode-cn.com/problems/powx-n/
题目名: 快速幂
实现Pow(x, n), 即计算x的n次幂函数
思路:
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(num):
            res = 1
            x_plus = x
            while num > 0:
                if num % 2:
                    res *= x_plus
                x_plus *= x_plus
                num //= 2
            return res
        return helper(n) if n >= 0 else 1.0 / helper(-n)


if __name__ == "__main__":
    s = Solution()
    print(s.myPow(5, 4))
