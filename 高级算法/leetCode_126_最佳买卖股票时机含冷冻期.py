"""
day: 2020-09-01
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xddkum/
题目名: 最佳买卖股票时机含冷冻期
给定一个整数数组,其中第i个元素代表了第i天的股票价格
设计一个算法计算出最大利润,在满足以下约束条件下,你可以尽可能地完成更多的交易:
    1. 你不能同时参与多笔交易(你必须在再次购买前出售掉之前的股票)
    2. 卖出股票后,你无法在第二天买入股票(冷冻期为1天)
示例:
    输入: [1, 2, 3, 0, 2]
    输出: 3
思路:
对于本题,在一天中,会有三种状态
    1. 今天不持有股票,且不处于冷冻期
    2. 今天持有股票
    3. 今天处于冷冻期
对于状态1,我们的转移条件是:
    1. 前一天持有股票,今天卖出,那么利润就是dp[i-1][1] + prices[i]
    2. 前一天不持有股票,今天不进行操作,那么利润就是dp[i-1][0]
    所以对于 dp[i][0],我们的状态转移方程是: dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
对于状态2,我们的转移条件是:
    1. 前一天持有股票,今天不进行操作,那么利润就是dp[i-1][1]
    2. 前一天处于冷冻期,今天买入,那么利润就是dp[i-1][2]-prices[i]
    所以: dp[i][1] = max(dp[i-1][1], dp[i-1][2]-prices[i])
对于状态3,我们的转移条件是:
    前一天不持有股票.
    所以: dp[i][2] = dp[i-1][0]
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        # 表示前一天不持股时的最大利润
        pre_1 = 0
        # 表示前一天持股时的最大利润
        pre_2 = -prices[0]
        # 表示前一天在冷冻期时的最大利润
        pre_3 = 0

        for i in range(1, n):
            # 不持股的状态由: 1.前一天不持股,今天不操作 2.前一天持股,今天卖出  两种状态转来,取他们之间的最大值
            curr_1 = max(pre_1, pre_2 + prices[i])
            # 持股的状态由: 1.前一天持股,今天不操作 2.前一天处于冷冻期,今天买入 两种状态转来,取他们之间的最大值
            curr_2 = max(pre_2, pre_3 - prices[i])
            # 冷冻期只能是前一天不持股(卖出操作)
            pre_3 = pre_1
            pre_1 = curr_1
            pre_2 = curr_2
        # 最终的最大利润,必然手上不持有股票,所以从状态1与状态3中取最大值
        return pre_1


if __name__ == "__main__":
    test = [1, 2, 3,  0, 2]
    s = Solution()
    print(s.maxProfit(test))
