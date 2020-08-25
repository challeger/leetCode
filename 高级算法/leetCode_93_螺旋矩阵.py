"""
day: 2020-08-25
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xw3ng2/
题目名: 除自身以外数组的乘积
题目描述: 给定一个包含m x n个元素的矩阵,请按照顺时针螺旋顺序,返回矩阵中的所有元素
示例:
输入:
    [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
输出: [1,2,3,6,9,8,7,4,5]
思路:
1. 标记法
    标记已经走过的元素,然后遍历的顺序是 右->下->左->上
    每次我们在当前格子判断下一步要走的方向,都优先走上一次走
    的方向,若上一次的方向不能走,那么按照顺序,走下一个方向
2. 收缩法
    每次输出矩阵最外层的元素,然后将矩阵向内收缩一层,直到不能收缩.
    输出最外层元素时,顺序为:
        1. 从左到右输出顶层元素
        2. 从上到下输出右侧元素
        3. 从右到左输出底层元素
        4. 从下到上输出左侧元素
    收缩时,左侧与顶层+1,右侧与底层-1即可
"""
from typing import List


class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # m = len(matrix)
        # if not m:
        #     return []
        # n = len(matrix[0])
        # # 判断该格子是否已经走过了
        # mask = [[False]*n for _ in range(m)]

        # x, y = 0, 0
        # total = m * n
        # dire_idx = 0
        # res = [0] * total
        # for i in range(total):
        #     res[i] = matrix[x][y]
        #     # 将当前格子标记为已走过
        #     mask[x][y] = True
        #     new_x, new_y = x + self.directions[dire_idx][0], y + self.directions[dire_idx][1]
        #     # 当前方向不能走,就走下一个方向
        #     if not (0 <= new_x < m and 0 <= new_y < n and not mask[new_x][new_y]):
        #         dire_idx = (dire_idx+1) % 4
        #     x += self.directions[dire_idx][0]
        #     y += self.directions[dire_idx][1]
        # return res
        m = len(matrix)
        if not m:
            return []
        n = len(matrix[0])
        res = []
        left, right, top, bottom = 0, n-1, 0, m-1
        while left <= right and top <= bottom:
            # 顶侧,从左到右
            for i in range(left, right+1):
                res.append(matrix[top][i])
            # 右侧,从上到下
            for i in range(top+1, bottom+1):
                res.append(matrix[i][right])
            if left < right and top < bottom:
                # 底侧,从右到左
                for i in range(right-1, left, -1):
                    res.append(matrix[bottom][i])
                # 左侧,从下到上
                for i in range(bottom, top, -1):
                    res.append(matrix[i][left])
            # 矩阵向内收缩一层
            left, right, top, bottom = left+1, right-1, top+1, bottom-1
        return res


if __name__ == "__main__":
    test = [[1, 2], [3, 4]]
    s = Solution()
    print(s.spiralOrder(test))
