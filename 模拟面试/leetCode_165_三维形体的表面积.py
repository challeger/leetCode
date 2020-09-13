"""
day: 2020-09-13
url: https://leetcode-cn.com/problems/surface-area-of-3d-shapes/
题目名:三维形体的表面积
在 N * N 的网格上,我们放置一些 1 * 1 * 1  的立方体

每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上

请你返回最终形体的表面积
思路:
    累加即可.
"""
from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    area = grid[i][j] * 4 + 2
                    if i > 0:
                        min_height = min(grid[i][j], grid[i-1][j])
                        area -= 2 * (min_height)
                    if j > 0:
                        min_height = min(grid[i][j], grid[i][j-1])
                        area -= 2 * (min_height)
                    res += area
        return res
