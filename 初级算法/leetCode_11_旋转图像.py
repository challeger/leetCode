"""
day: 2020-08-11
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnhhkv/
题目名: 旋转图像
题目描述: 给定一个NxN的二维矩阵表示一个图像,将图像顺时针旋转90度
必须直接修改输入的二维矩阵
示例:
    输入:
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    旋转后:
    [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]
思路:
1. zip
    观察可知,旋转后,第一列变为第一行,第二列变为第二行,第三列变为第三行..
    所以使用zip函数将二维矩阵的每一列构成一个新的列表,然后翻转过来,最后组成
    旋转后的矩阵.

2. 对称翻转
    将矩阵沿左上角到右下角的中间线翻转,然后再将每一行翻转,效果等同于顺时针旋转90度

3. 矩阵旋转
    逐层旋转矩阵,例如3x3的矩阵为2层; 4x4的矩阵也为2层
    将一个矩阵分为几层的公式为 length // 2 + length % 2
    然后依次旋转四个矩阵块,
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]
    第一次旋转 1(0, 0)->3(0, 2)->9(2, 2)->7(2, 0)->1(0, 0)
    [7, 2, 1]
    [4, 5, 6]
    [9, 8, 5]
    第二次旋转 2(0, 1)->6(1, 2)->8(2, 1)->5(1, 0)->2(0, 1)
    [7, 4, 1]
    [8, 5, 2]
    [9, 6, 5]
    第三次旋转 5(1, 1) -> 5(1, 1)
    可以发现,每次选择,矩阵块(x, y)的旋转目标点坐标是(y, length-1-x),四个矩阵块构成一次循环
    所以我们就可以通过循环,每次旋转四个矩阵块,最终完成矩阵的旋转
"""


class Solution:
    @staticmethod
    def rotate(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 解法1
        # matrix[:] = map(list, zip(*matrix[::-1]))
        length = len(matrix[0])

        # 解法2
        # 将数组沿对角线置换
        # for i in range(length):
        #     for j in range(i, length):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 翻转每一行
        # for i in range(length):
        #     matrix[i].reverse()

        # 解法3
        for i in range(length // 2 + length % 2):
            for j in range(length // 2):
                matrix[length-1-j][i], matrix[length-1-i][length-1-j], matrix[j][length-1-i], matrix[i][j] =\
                    matrix[length-1-i][length-1-j], matrix[j][length-1-i], matrix[i][j], matrix[length-1-j][i]


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution.rotate(matrix)
    print(matrix)
