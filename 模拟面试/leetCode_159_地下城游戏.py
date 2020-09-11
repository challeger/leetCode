"""
day: 2020-09-11
url: https://leetcode-cn.com/problems/dungeon-game/
题目名: 地下城游戏
一些恶魔抓住了公主（P）并将她关在了地下城的右下角.地下城是由 M x N 个房间组成的二维网格.
我们英勇的骑士（K）最初被安置在左上角的房间里,他必须穿过地下城并通过对抗恶魔来拯救公主.
骑士的初始健康点数为一个正整数.如果他的健康点数在某一时刻降至 0 或以下,他会立即死亡.
有些房间由恶魔守卫,因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数,则表示骑士将损失健康点数）;
其他房间要么是空的（房间里的值为 0）,要么包含增加骑士健康点数的魔法球（若房间里的值为正整数,则表示骑士将增加健康点数.
为了尽快到达公主,骑士决定每次只向右或向下移动一步
编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数.

例如,考虑到如下布局的地下城,如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下,则骑士的初始健康点数至少为 7.
[
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
]
思路:
    如果我们从起点来进行状态转移,需要记录两个关键值,
    一个是从出发点到当前点的路径和,一个是从出发点到当前点所需的最小初始值.
    如果我们从终点开始进行状态转移,用dp[i][j]表示从坐标(i, j)到达终点需要的最小血量,那么我们
    无需记录路径和,因为只要我们的路径和不小于dp[i][j],就能到达终点,
"""
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])

        # dp表示到达dungeon[i][j]需要的最小初始值
        dp = [[float('inf')] * (n+1) for _ in range(m+1)]
        dp[m][n-1] = dp[m-1][n] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # 选择需要血量较少的路径
                min_hp = min(dp[i+1][j], dp[i][j+1])
                # 如果dungeon是个回血包,到达这个格子之前他的血量至少要为1
                dp[i][j] = max(min_hp-dungeon[i][j], 1)
        return dp[0][0]


s = Solution()
print(s.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
