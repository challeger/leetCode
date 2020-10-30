"""
day: 2020-10-30
url: https://leetcode-cn.com/problems/island-perimeter/
题目名: 岛屿的周长
给定一个包含 0 和 1 的二维网格地图,其中 1 表示陆地 0 表示水域.

网格中的格子水平和垂直方向相连（对角线方向不相连）.
整个网格被水完全包围,但其中恰好有一个岛屿（或者说,一个或多个表示陆地的格子相连组成的岛屿）.

岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）.格子是边长为 1 的正方形.
网格为长方形,且宽度和高度均不超过 100 .计算这个岛屿的周长.

示例:
    输入:
    [[0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]]

    输出:
    16

思路:
依次遍历,如果当前格子是陆地,就判断他左边和上面是否有也是陆地,是则-2
"""
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        if not n:
            return res
        m = len(grid[0])
        for x in range(n):
            for y in range(m):
                if grid[x][y]:  # 如果为1
                    res += 4
                    if x and grid[x-1][y]:
                        res -= 2
                    if y and grid[x][y-1]:
                        res -= 2
        return res
