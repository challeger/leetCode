"""
day: 2020-08-10
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2zsx1/
题目名: 买卖股票的最佳时机
题目描述: 给定数组,它的第i个元素是一支给定股票的第i天的价格
设计一个算法来计算你能获取的最大利润(可以多次买卖一支股票)(再次购买股票前必须出售掉之前的股票)
示例:
    给定nums = [7,1,5,3,6,4]
    在第2天(股票价格 = 1)时买入, 第3天(股票价格 = 5)时卖出, 利润为4
    在第4天(股票价格 = 3)时买入, 第5天(股票价格 = 6)时卖出, 利润为3
    总利润为 7
思路:
1. 贪心算法:
    明天的股票价格-今天的股票价格 > 0,则进行交易,否则不交易,最终将每次交易的利润相加得到总利润.
    但这种算法只能得到最大利润,并不能得到具体的交易流程,比如[1, 2, 3, 4, 5],最终利润是4,
    交易流程应该是第一天买,最后一天卖,但在我们的计算过程中,是分为了四次交易来进行利润计算的.
"""


class Solution(object):
    @staticmethod
    def maxProfit(prices):
        return sum(b - a for a, b in zip(prices, prices[1:]) if b > a)


if __name__ == "__main__":
    foo = [7,1,5,3,6,4]
    print(Solution.maxProfit(foo))
