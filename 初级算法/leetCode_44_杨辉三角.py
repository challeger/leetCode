"""
day: 2020-08-15
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xncfnv/
题目名: 杨辉三角
题目描述: 给定一个非负整数nomRows, 生成杨辉三角的前NumRows行
在杨辉三角中,每个数是它左上方和右上方的数的和
示例:
    输入: 5
    输出:
    [
          [1],
         [1,1],
        [1,2,1],
       [1,3,3,1],
      [1,4,6,4,1]
    ]
思路:
1. 在构建每一层时,每一层的长度既是当前层数,构建一个指定长度的数组,然后将数组的首部和尾部置1
从第二位数字开始,第i位数字为上一层的第i-1位数字+第i位数字
2. 可以发现,每一层的数组,其实是上一层的数组错位相加得到的,例如:
    [1, 3, 3, 1] -> [1, 2, 1, 0] + [0, 1, 2, 1]
    所以我们每次循环,直接将上一层数组首位+[0]与末尾+[0],然后各位相加即可
"""


class Solution:
    def generate(self, numRows: int) -> list:
        # result = []
        # for i in range(numRows):
        #     foo = [None] * (i + 1)
        #     foo[0], foo[-1] = 1, 1
        #     for j in range(1, i):
        #         foo[j] = result[i-1][j] + result[i-1][j-1]
        #     result.append(foo)
        # return result
        if numRows:
            result = [[1]]
            while len(result) < numRows:
                foo = [a+b for a, b in zip([0]+result[-1], result[-1]+[0])]
                result.append(foo)
            return result
        return []


if __name__ == "__main__":
    s1 = Solution()
    test = 5
    print(s1.generate(test))
