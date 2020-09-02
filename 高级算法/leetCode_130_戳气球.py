"""
day: 2020-09-02
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xdiww6/
题目名: 戳气球
有n个气球,编号为0到n-1,每个气球上都标有一个数字,这些数字存在数组nums中.
现在要求你戳破所有的气球.如果你戳破气球i,就可以获得nums[left]*nums[i]*nums[right]个硬币.这里的left和right
代表和i相邻的两个气球的序号.注意当你戳破了气球i后,🎈left和🎈right就变成了相邻的气球.求能获得硬币的最大数量
示例:
    输入: [3, 1, 5, 8]
    输出: 167
    解释: coins = 3*1*5 + 3*5*8 + 1*3*8 + 1*8*1
思路:
    我们戳爆气球的所有收益,是戳爆该气球的收益+左边所有气球的收益+右边所有气球的收益
    而左边所有气球的收益,则是戳爆左边气球的最后一个气球后,它的左边气球的收益,与右边气球的收益..
    也就是说,我们可以按照这个规律将问题一路划分下去,从求戳爆所有气球的最大收益,减到求戳爆一个气球的最大收益.
1. 递归
    我们在数组左边与右边分别添加一个1,来方便计算,然后不停对一个指定的区间求它的最大收益..
    求法: 遍历这个区间中的所有气球,我们尝试将当前气球i作为最后一个戳爆的气球,那么戳爆气球i的收益就是val[left]*val[i]*val[right],
    而在这之前,我们已经戳爆了左边区间的所有气球,与右边区间的所有气球,所以我们最后戳爆这个气球的总收益应该是:
        total = 左边区间的最大收益+当前气球i收益+右边区间的最大收益,当区间的左边界=右边界时,表示我们没有气球可戳了,返回0.
    最终我们取遍历中得到的最大的total..
    在写递归时,我们要将递归的函数当做一个已经返回结果的变量.

2. 动态规划
    整体思想不变,都是分治,对于区间(i, j)的最大收益,必然是戳爆某个气球k后的收益,对于
    戳爆气球k的收益,应该是 (i, k)的最大收益+k的收益+(k, j)的收益,我们自底向上的计算dp,
    dp[i][j]表示左边界为i,右边界为j的区间的最大收益
    首先包含0个气球的区间必然都是0, 包含1个气球的区间,在戳爆该气球后,它的左区间和右区间都是0个气球的区间,
    可以使用已经赋好的值来计算..包含2个气球的区间,再戳爆一个气球后,左区间与右区间之间必然有一个包含1个气球,就可以
    利用上一次循环计算好的1个气球的区间的最大收益来计算,以此类推,直到计算包含了所有气球的区间,也就是dp[0][-1]
"""
from typing import List
from functools import lru_cache


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        val = [1] + nums + [1]

        @lru_cache(None)
        def solve(left, right):
            # 如果左边界大于等于右边界-1,说明,区间中不会有可戳爆的气球,收益为0
            if left >= right - 1:
                return 0
            best = 0
            for i in range(left+1, right):
                # 最后一个戳本次气球获得的硬币数量
                total = val[left] * val[i] * val[right]
                # 戳区间两边的气球能获得的最大硬币数量
                total += solve(left, i) + solve(i, right)
                best = max(best, total)
            return best
        return solve(0, n+1)

    def maxCoins_dp(self, nums: List[int]) -> int:
        val = [1] + nums + [1]
        n = len(val)
        # dp[i][j]表示,区间(i, j)戳气球能得到的最大收益,注意是开区间,因为 最左侧的1与最右侧是1是我们补上去的,是不能戳的
        dp = [[0]*(n) for _ in range(n)]

        def range_best(left, right):
            # 尝试将区间内的每一个气球作为最后一个戳爆的气球,计算收益
            # 取他们之间的最大值
            for k in range(left+1, right):
                temp = dp[left][k] + val[left]*val[k]*val[right] + dp[k][right]
                dp[left][right] = max(dp[left][right], temp)
        # 对于一个从left到right的开区间,最后一个戳气球k的总收益
        # 应该是dp[left][k]+val[left]*val[k]*val[right]+dp[k][right]的收益
        # 我们可以尝试该区间中的每一个气球,将其作为最后一个去戳的气球,然后取得到的收益的最大值
        # 最后计算得到的,dp[0][-1]就是从开始到结尾作为区间的最大收益
        # 因为是开区间,能戳气球的区间长度至少为1,那么右边界应该至少是左边界+2
        for i in range(2, n):
            # 计算该区间的最大收益
            for j in range(0, n-i):
                range_best(j, i+j)
        return dp[0][-1]


if __name__ == "__main__":
    test = [3, 1, 5, 8]
    s = Solution()
    print(s.maxCoins_dp(test))
