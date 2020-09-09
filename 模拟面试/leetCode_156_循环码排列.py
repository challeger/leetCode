"""
day: 2020-09-09
url: https://leetcode-cn.com/problems/circular-permutation-in-binary-representation/
题目名: 循环码排列
给你两个整数n和start,你的任务是返回任意(0, 1, 2, ..., 2^n-1)的排列p,并且满足
    p[0] = start
    p[i] 与 p[i+1] 的二进制表示形式只有一位不同
    p[0] 和 p[2^n-1] 的二进制表示也只有一位不同
示例:
    输入: n = 2, start = 3
    输出: [3,2,0,1]

思路:
    格雷码 + 旋转数组
"""
from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res = [0]
        head = 1
        # 求出格雷码
        for _ in range(n):
            for i in range(len(res)-1, -1, -1):
                res.append(res[i]+head)
            head <<= 1
        # 找到索引
        index = res.index(start)
        # 旋转数组
        res[:] = res[index:] + res[:index]
        return res
