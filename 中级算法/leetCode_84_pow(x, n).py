"""
day: 2020-08-23
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xwo102/
题目名: pox(x, n)
题目描述: 实现pow(x, n),即计算x的n次幂函数
示例:
    输入: 2.0000, 10
    输出: 1024.0000
    输入: 2.10000, 3
    输出: 9.26100
    输入: 2.00000 -2
    输出: 0.25000
思路:
1. 递归
    n^10 = n^5*n^5, n^11 = n^5*n^5*n
    当目前的幂次x是偶数时,n^x = n^(x//2)*n^(x//2)
    当目前的幂次x是奇数时,n^x = n^(x//2)*n^(x//2)*n
    所以我们要计算n^x时,可以递归的向下计算出n^(x//2),然后根据
    当前的x是奇数还是偶数,做出相应的计算,当x=0时,返回1
2. 迭代
    迭代的难点在于,我们不知道计算下一次的幂要不要多乘一个n
    对于x^77, 77的二进制为(1001101),所以77 = 2^1 + 2^4 + 2^8 + 2^64
    我们定义一个变量来表示当前二进制位的2^n次幂,若当前的位为1,则
    res *= x^(2^n),否则继续计算下一位的次幂..直到计算到0
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(num):
            # if num == 0:
            #     return 1.0
            # mid = helper(num // 2)
            # return mid * mid if not num % 2 else mid * mid * x
            ans = 1.0
            # 表示当前迭代到的num的二进制第n位的,x^n
            x_plus = x
            while num > 0:
                # 如果当前位上为1
                if num % 2:
                    # 将当前位的次幂乘到结果中
                    ans *= x_plus
                # 否则计算下一位
                x_plus *= x_plus
                # 右移一位
                num = num >> 1
            return ans
        return helper(n) if n >= 0 else 1.0 / helper(-n)


if __name__ == "__main__":
    test1 = 2.0
    test2 = 10
    s = Solution()
    print(s.myPow(test1, test2))
