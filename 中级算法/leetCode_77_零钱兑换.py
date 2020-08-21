"""
day: 2020-08-21
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvf0kh/
题目名: 零钱兑换
题目描述: 给定不同面额的硬币coins和一个总金额amount,编写一个函数计算可以凑成总金额所需
的最少的硬币个数,如果没有组合能组成总金额,返回-1
示例:
    输入: coins = [1, 2, 5], amount = 11
    输出: 3
    输入: coins = [2], amount = 3
    输出: -1
思路:
1. 暴力+剪枝
    将硬币面额数组按从大到小排序,我们想要少的使用硬币数,应该优先使用大面额硬币
    所以我们先使用大硬币,直到再使用大硬币会超出总额时,就递归下一层,丢面额稍小的硬币.

    对于丢大硬币,我们可以采用balance // coins[i]来计算我们最多可以丢多少枚大硬币,若
    因为丢的过多无法凑出总额,就回溯减少大硬币的数量.

    因为我们第一个找到的不一定就是最优解,所以还是得将所有结果递归完,当我们在计算丢硬币的数量时,
    若在某一层递归中,我们当前的硬币数量已经超过了之前计算出来的结果的硬币数量,那么就可以直接结束这次
    计算,因为无论如何都已经不是最优解了
2. 动态规划
凑出i元钱所需的最少硬币,应该是凑出i-coin钱所需的最少硬币+1,
    dp[i] = min(dp[i-coin]+1, float('inf'))
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # self.ans = float('inf')

        # def dfs(coind, balance, count):
        #     if not balance:
        #         self.ans = min(self.ans, count)
        #         return
        #     if coind >= len(coins):
        #         return
        #     for i in range(balance // coins[coind], -1, -1):
        #         if i + count < self.ans:
        #             dfs(coind+1, balance-coins[coind]*i, count+i)
        #         else:
        #             break
        # coins.sort()
        # coins.reverse()
        # dfs(0, amount, 0)
        # return self.ans if self.ans != float('inf') else -1
        # 设为amount+1的原因是,如果有结果,它的最大值应该是amount,所以amount类似于float('inf')
        dp = [amount+1 for _ in range(amount+1)]
        dp[0] = 0
        # 遍历在所有状态的所有取值
        for i in range(amount+1):
            # 求出所有选择中的最小值
            for coin in coins:
                # 该选择行不通,跳过
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i-coin])
        # 若值是amount+1,说明无法凑出该金额,所以返回-1,否则返回dp[amount]
        return -1 if dp[amount] == amount+1 else dp[amount]


if __name__ == "__main__":
    test1 = [186, 419, 83, 408]
    money = 6249
    s = Solution()
    print(s.coinChange(test1, money))
