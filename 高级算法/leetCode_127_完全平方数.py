"""
day: 2020-09-01
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xd03l1/
题目名: 完全平方数
给定正整数n,找到若干个完全平方数(比如1, 4, 9, 16, ..), 使得它们的和等于n.你需要让组成和的
完全平方数的个数最少
示例:
    输入: 12
    输出: 3
    解释: 12 = 4 + 4 + 4
    输入: 13
    输出: 2
    解释: 13 = 4 + 9
思路:
1. 动态规划
    对于dp[i]需要的完全平方数,对于某个平方数num,dp[i]=dp[i-num]+1,依次遍历所有在i范围内的完全平方数
    让dp[i]取他们之中的最小值.
2. 暴力枚举+剪枝+dfs
    我们要想尽可能使用少的完全平方数,那么应该优先使用较大的完全平方数,那么我们每次都选择可以选择
    的最大完全平方数,并计算最多可以选择多少个最大完全平方数,也就是 n // max_square, 然后让
    n - max_square*use_count, 去再用下一个完全平方数去计算得到的值..
    若在某一层计算中,当前的count总数已经超过了之前计算得到的count,那么就直接结束本次计算,因为无论
    如何得到的结果都不会小于之前得到的count
3. bfs
    从n开始,将n减去每个完全平方数得到的结果加入下一层中,如果有一层square == num,那么当前层就是
    最少个数.
4. 数学方法
    当数字n=4^k(8m+7)时,只能由四个平方数组成,直接返回4
    否则判断它本身是否是一个完全平方数,是则返回1
    否则枚举0-n范围内的所有完全平方数,使n-i*i,判断该值是否是一个完全平方数,是则返回2
    否则返回3
"""


class Solution:
    def numSquares(self, n: int) -> int:
        # 0-n中所有完全平方数
        square_nums = [i**2 for i in range(int(n**0.5)+1)]
        dp = [n+1 for _ in range(n+1)]
        dp[0] = 0
        for i in range(1, n+1):
            for square in square_nums:
                if i < square:
                    break
                # 当前需要的完全平方数数量,是减去当前完全平方数之后,需要的数量+1
                dp[i] = min(dp[i-square]+1, dp[i])
        return dp[n]

    def numSquares_dfs(self, n: int) -> int:
        self.ans = float('inf')
        square_nums = [i**2 for i in range(int(n**0.5)+1, 0, -1)]

        def dfs(square, balance, count):
            if not balance:
                self.ans = min(self.ans, count)
                return
            if square >= len(square_nums):
                return
            for i in range(balance // square_nums[square], -1, -1):
                if i + count < self.ans:
                    dfs(square+1, balance-square_nums[square]*i, count+i)
                else:
                    break

        dfs(0, n, 0)
        return self.ans

    def numSquares_bfs(self, n: int) -> int:
        square_nums = [i**2 for i in range(1, int(n**0.5)+1)]
        level = 0
        queue = {n}
        while queue:
            level += 1
            next_queue = set()
            for num in queue:
                for square in square_nums:
                    # 找到了,直接返回楼层层数
                    if square == num:
                        return level
                    # 大于num,说明后面的所有完全平方数都比num大,所以直接退出
                    # 减少计算量
                    elif square > num:
                        break
                    # 否则加入下一层
                    else:
                        next_queue.add(num-square)
            queue = next_queue
        return level

    def numSquares_math(self, n: int) -> int:
        def isSquare(num):
            sq = int(num ** 0.5)
            return sq*sq == num

        # 判断是否符合四平方数公式
        while (n & 3) == 0:
            n >>= 2
        if (n & 7) == 7:
            return 4
        # 判断是否是一个完全平方数
        if isSquare(n):
            return 1
        # 判断是否是两个完全平方数的和
        for i in range(1, int(n**0.5)+1):
            if isSquare(n-i*i):
                return 2
        return 3


if __name__ == "__main__":
    test = 12
    s = Solution()
    print(s.numSquares_bfs(test))
