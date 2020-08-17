"""
day: 2020-08-17
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvmy42/
题目名: 矩阵置零
题目描述: 给定一个 m x n 的矩阵,如果一个元素为0,则将其所在行和列的所有元素都设为.请使用原地算法
示例:
    输入:
    [
      [1,1,1],
      [1,0,1],
      [1,1,1]
    ]
    输出:
    [
      [1,0,1],
      [0,0,0],
      [1,0,1]
    ]
思路:
1. 遍历数组,用字典记录出现0的行与列,最后再次遍历并置换
2. 用数组的第一行与第一列来记录该行是否需要置零,因为第一行与
第一列的标记元素是同一个,所以需要额外定义一个变量来记录第一列
是否需要置零,第一遍遍历标记完成后,从第二列与第二行开始,将需要置零
的行与列置零,然后判断第一行是否需要置零,最后判断第一列是否需要置零
"""


class Solution:
    def setZeroes(self, matrix: list):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # row_length = len(matrix[0])
        # col_length = len(matrix)
        # zeros = {
        #     'row': set(),
        #     'col': set(),
        # }
        # foo = 0
        # while foo < row_length or foo < col_length:
        #     row, col = 0, 0
        #     while row < row_length and foo < col_length:
        #         if matrix[foo][row] == 0:
        #             zeros['row'].add(foo)
        #         row += 1
        #     while col < col_length and foo < row_length:
        #         if matrix[col][foo] == 0:
        #             zeros['col'].add(foo)
        #         col += 1
        #     foo += 1
        # for i in zeros['row']:
        #     matrix[i][:] = [0]*row_length
        # for i in zeros['col']:
        #     for row in matrix:
        #         row[i] = 0
        sign_first_col = False
        rol_len = len(matrix)
        col_len = len(matrix[0])
        for i in range(rol_len):
            if matrix[i][0] == 0:
                sign_first_col = True
            for j in range(1, col_len):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, rol_len):
            for j in range(1, col_len):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        if not matrix[0][0]:
            matrix[0][:] = [0] * col_len
        if sign_first_col:
            for i in range(rol_len):
                matrix[i][0] = 0


if __name__ == "__main__":
    s1 = Solution()
    test = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    s1.setZeroes(test)
    print(test)
