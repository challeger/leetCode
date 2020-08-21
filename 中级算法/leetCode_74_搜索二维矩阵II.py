"""
day: 2020-08-21
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xv11yj/
题目名: 搜索旋转排序数组
题目描述: 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
    每行的元素从左到右升序排列。
    每列的元素从上到下升序排列。
示例:
    matrix:[
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    输入: target = 5
    输出: true
    输入 target = 20
    输出: false
思路:
1. 从左下角开始查找
    若从左下角开始查找,那么往上走数会变小,往右走数会变大
    我们根据当前格子元素x与target进行对比,
    若x>target, 则往上走
    若x<target, 则往右走
    若x==target,则返回true
    若遍历完还没找到,则返回false
2. 四分矩阵
    我们从矩阵的列中心向下寻找,若nums[row][mid]大于target,那么说明
    该点左上的矩阵(因为该点的上一个点小于目标点,所以左上矩阵的值都小于目标点)
    与右下的矩阵(因为右下矩阵的开始点大于目标点,所有右下矩阵的值都大于目标点)
    都不可能存在我们要的目标点
"""


class Solution:
    directions = [(1, 0), (0, 1)]

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # m = len(matrix)
        # if not m:
        #     return False
        # n = len(matrix[0])
        # if not n:
        #     return False
        # row = m - 1
        # col = 0
        # while row >= 0 and col < n:
        #     if matrix[row][col] < target:
        #         col += 1
        #     elif matrix[row][col] > target:
        #         row -= 1
        #     else:
        #         return True
        # return False

        if not matrix:
            return False

        def helper(left, up, right, down):
            # 若越界了,或者target不在矩阵范围内,则直接返回False
            if left > right or up > down:
                return False
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False

            # 矩阵的行中心点,会遍历这行所在的列
            mid = (left + right) >> 1
            row = up
            # 一直遍历到底或者中心点>目标值
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            # 找左下与右上.
            return helper(left, row, mid-1, down) or helper(mid+1, up, right, row-1)
        return helper(0, 0, len(matrix[0])-1, len(matrix)-1)


if __name__ == "__main__":
    test = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    test1 = 1
    s = Solution()
    print(s.searchMatrix(test, test1))
