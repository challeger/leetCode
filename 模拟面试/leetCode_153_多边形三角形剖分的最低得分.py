"""
day: 2020-09-08
url: https://leetcode-cn.com/problems/minimum-score-triangulation-of-polygon/
题目名: 三角形剖分的最低得分
给定N,想象一个凸N边多边形,其顶点按顺时针顺序依次标记为A[0], A[i], ... A[N-1].
假设您将多边形剖分为N-2个三角形,对于每个三角形,该三角形的值是顶点标记的乘积,三角形
剖分的分数是进行三角剖分后所有N-2个三角形的值之和

返回多边形进行三角剖分后可以得到的最低分
思路:
动态规划:
    对于一个四边形,它的得分,是以它中间的一个端点为起点,将四边形划分得到的两个三角形的和
    取中间的最小值..
    我们定义一个dp, dp[i][j]表示以i为起点,j为终点的最低分得分,那么对于 j - i < 2的所有值
    他们无法组成三角形,所以值为0
    而dp[i][j]的值, 应该是在[i+1, j-1]中取一个点,将它作为新的分割线,
    得到的三角形A[i]*A[k]*A[j]得到的分值+被分割后的dp[i][k]和dp[k][j]的值,取他们之中的最小值
    最终答案就是dp[0][-1]
"""
from typing import List


class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        n = len(A)
        dp = [[0]*n for _ in range(n)]

        for size in range(2, n):
            for i in range(n-size):
                j = i + size
                dp[i][j] = float('inf')
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j]+A[i]*A[j]*A[k])
        return dp[0][-1]


if __name__ == "__main__":
    test = [1, 3, 1, 4, 1, 5]
    s = Solution()
    print(s.minScoreTriangulation(test))
