"""
day: 2020-09-06
url: https://leetcode-cn.com/problems/count-servers-that-communicate/
题目名: 统计参与通信的服务器
这里有一幅服务器分布图,服务器的位置标识在 m * n 的整数矩阵网格 grid 中,1 表示单元格上有服务器,0 表示没有.
如果两台服务器位于同一行或者同一列,我们就认为它们之间可以进行通信.
请你统计并返回能够与至少一台其他服务器进行通信的服务器的数量.
示例:
    输入: grid = [[1, 0], [0, 1]]
    输出: 0
    输入: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
    输出: 4
思路:
1. 两次遍历
    第一次遍历记录每一行与每一列的计算机数量,第二次遍历,如果遇到计算机
    判断它所在的行与列是否有超过两台的计算机,是则+1.
"""
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count_m = [0] * m
        count_n = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count_m[i] += 1
                    count_n[j] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (count_m[i] > 1 or count_n[j] > 1):
                    ans += 1
        return ans


if __name__ == "__main__":
    test = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    s = Solution()
    print(s.countServers(test))
