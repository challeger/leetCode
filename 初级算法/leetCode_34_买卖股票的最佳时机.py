"""
day: 2020-08-14
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn8fsh/
题目名: 买卖股票的最佳时机
题目描述: 给定一个数组,它的第i个元素是一支给定股票的第i天的价格
如果你最多只允许完成一笔交易, 设计一个算法来计算你所能获得的最大利润
示例:
    输入: [7, 1, 5, 3, 6, 4]
    输出: 5  第2天买入,第5天卖出, 6-1 = 5
    输入: [7, 6, 5, 4]
    输出: 0 没有利润可赚
思路:
1.
    定义两个变量,分别记录最低的价格与最高的利润,每次循环,将当天的价格-最低的价格,与最高利润
    去比较,然后当天的价格再与最低的价格去比较,遍历完之后的maxprofit就是最高利润
2. 状态机
    对于本题,我们会有两种状态, 天数, 当前的持有状态(用1表示持有,0表示没有持有)
    那么,我们用一个二维数组就可以装下这几种状态的组合:
        dp[i][0 or 1]
    0 <= i <= n-1, n表示天数
    dp[1][1]的含义就是: 第2天,手上持有股票
    dp[2][0]的含义就是: 第3天,手上未持有股票
    我们最终的答案是dp[n-1][0],即最后一天手上未持有股票时,最多获得多少利润
    那么我们当天不持有的最大利润, 应该是前一天未持有股票时的最大利润(rest行为), 
    前一天持有股票并今天卖出的最大利润,进行对比,取最大值
    当天持有股票的最大利润,应该是前一天持有股票的利润,与今天买入股票所需的利润,取最大值
"""


class Solution:
    @staticmethod
    def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit
        # if prices:
        #     n = len(prices)
        #     dp = [[0, 0] for _ in range(n)]
        #     for i in range(n):
        #         if i == 0:
        #             dp[i][0] = 0
        #             dp[i][1] = -prices[i]
        #             continue
        #         dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        #         dp[i][1] = max(dp[i-1][1], -prices[i])
        #     return dp[n-1][0]
        # return 0


if __name__ == "__main__":
    test = [2, 3, 1, 5, 3, 6, 5]
    print(Solution.maxProfit(test))
