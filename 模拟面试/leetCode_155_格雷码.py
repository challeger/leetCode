"""
day: 2020-09-09
url: https://leetcode-cn.com/problems/gray-code/
题目名: 格雷编码
格雷编码是一个二进制数字系统，在该系统中,两个连续的数值仅有一个位数的差异。
给定一个代表编码总位数的非负整数 n,打印其格雷编码序列.即使有多个不同答案,你也只需要返回其中一种.
格雷编码序列必须以 0 开头。

示例:
    输入: 2
    输出: [0,1,3,2]
    解释:
        00 - 0
        01 - 1
        11 - 3
        10 - 2
思路:
    设n阶格雷码为G(n),那么G(n+1)阶的格雷码为:
        1.给G(n)阶格雷码每个元素二进制形式前面添加0,得到G'(n)
            比如G(1) = [0, 1], 那么G'(1) = [00, 01]
        2.将G(n)集合倒序为R(n), 给R(n)每个元素二进制形式前面添加1,得到R'(n)
            比如G(1) = [0, 1], 那么R(1) = [1, 0], R'(1) = [11, 10]
        3.G(n+1) = G'(n) 与 R'(n)的并集

    因为最高位默认为0,所以G'(n) = G(n),那么我们只需要循环n次,每次计算要添加1的位数head,
    然后倒序遍历res数组,让数组中每一个数都+head,然后添加到res数组中,最终得到的res数组就是
    我们要的结果了.
"""
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res, head = [0], 1
        for i in range(n):
            # 计算R'(n),并添加到数组中
            for j in range(len(res)-1, -1, -1):
                res.append(head+res[j])
            # 下次要加1的位数在当前的左边一位.
            head <<= 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.grayCode(2))
