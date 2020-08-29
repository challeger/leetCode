"""
day: 2020-08-29
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xde3ji/
题目名: 矩阵中的最长递增路径
给定一个整数矩阵,找出最长递增路径的长度.
对于每个单元格,你可以往上下左右四个方向移动,你不能在对角线方向上移动或移动到边界外.
示例:
    输入:
    [
    [9,9,4],
    [6,6,8],
    [2,1,1]
    ]
    输出: 4
    解释: [1, 2, 6, 9]
思路:
1. 记忆化+深度优先搜索
    lru_cache函数的作用是将函数执行的结果保存起来,在传入相同的参数时,可以直接返回结果..
    类似于用哈希表将参数:结果 存储了起来
    所以我们只需要深度遍历数组的每一个节点即可
2. 出度表+广度优先搜索
    出度: 以该节点为出发点的边的总数
    在本题中,出度为0,表示该节点周围已经没有比它大的元素了,那么就将其加入下一层要遍历的队列中
    可以将其理解为,从递增序列中倒序遍历,最终遍历的层数就是序列的最大长度.
"""
from typing import List
from collections import deque
from functools import lru_cache


class Solution:
    directions = [(1, 0),  (0, 1), (-1, 0), (0, -1)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])

        @lru_cache(None)
        def dfs(x, y):
            max_depth = 1
            for direction in self.directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if 0 <= new_x < m and 0 <= new_y < n and matrix[new_x][new_y] > matrix[x][y]:
                    max_depth = max(max_depth, dfs(new_x, new_y)+1)
            return max_depth

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res

    def longestIncreasingPath_bfs(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        # 出度表
        # 出度: 以该节点为出发点的路径的总数
        # 在本题中,出度为0表示该节点周围已经没有比它大的元素了.
        out_deq = [[0]*n for _ in range(m)]
        queue = deque()
        # 建立出度表,并将当前所有出度为0的节点加入队列中
        for i in range(m):
            for j in range(n):
                for direction in self.directions:
                    new_i = i + direction[0]
                    new_j = j + direction[1]
                    if 0 <= new_i < m and 0 <= new_j < n and matrix[new_i][new_j] > matrix[i][j]:
                        out_deq[i][j] += 1
                if not out_deq[i][j]:
                    queue.append((i, j))

        ans = 0
        # 依次访问出度为0的节点,遍历该节点周围的四个节点,将他们的出度-1,代表正在走该路线..
        # 若出度-1后,出度变为0,那么说明该节点周围已经没有比它大的元素了,将其加入队列.
        # 搜索结束时,搜索的总层数也就是递增路径的最大长度
        while queue:
            ans += 1
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                for direction in self.directions:
                    new_i = i + direction[0]
                    new_j = j + direction[1]
                    if 0 <= new_i < m and 0 <= new_j < n and matrix[new_i][new_j] < matrix[i][j]:
                        out_deq[new_i][new_j] -= 1
                    if not out_deq[i][j]:
                        queue.append((i, j))
        return ans


if __name__ == "__main__":
    test = [
        [3, 4, 5],
        [3, 2, 6],
        [2, 2, 1]
    ]
    s = Solution()
    print(s.longestIncreasingPath(test))
