"""
day: 2020-08-15
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnzlu6/
题目名: 计数素数
题目描述: 统计所有小于非负整数n的质数的数量
示例:
    输入: 10
    输出: 4
    2, 3, 5, 7
思路:
设一个数组isPrime,里面的值全为1,并把isPrime[0]和isPrime[1]置为0(0和1不是质数)
从2开始进行遍历时,若isPrime[i]==1,则可以把从i^2开始, 每隔i步就把isPrime[i]的值置为0
从i^2开始的原因是,i^2之前的非质数已经被置为0,所以无需再次复制.
    isPrime[i*i:n:i] = [0] * ((n-1-i*i) // i + 1)
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n > 2:
            isPrime = [1] * n
            isPrime[0] = isPrime[1] = 0
            for i in range(2, int(n ** 0.5)+1):
                if isPrime[i]:
                    isPrime[i*i:n:i] = [0] * ((n-1-i*i) // i + 1)
            return sum(isPrime)
        else:
            return 0
        # def is_primes(num):
        #     for i in range(2, int(math.sqrt(num))+1):
        #         if num % i == 0:
        #             return False
        #     return True
        # count = 0
        # if n > 2:
        #     for i in range(2, n):
        #         if is_primes(i):
        #             count += 1
        # return count


if __name__ == "__main__":
    s = Solution()
    print(s.countPrimes(10))
