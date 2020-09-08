"""
day: 2020-09-08
url: https://leetcode-cn.com/problems/find-positive-integer-solution-for-a-given-equation/
题目名: 找出给定方程的正整数解
给出一个函数  f(x, y) 和一个目标结果 z，请你计算方程 f(x,y) == z 所有可能的正整数 数对 x 和 y。
给定函数是严格单调的，也就是说：
f(x, y) < f(x + 1, y)
f(x, y) < f(x, y + 1)
思路:
"""
from typing import List


"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
"""


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        left = 1
        right = 1000
        ans = []
        # 从左到右以及从右到左扫描数组[1, 1000]
        while left <= 1000 and right >= 1:
            tmp = customfunction.f(left, right)
            # 如果得到的值比z大,说明正确的值在左边,所以减少right的值
            if tmp > z:
                right -= 1
            # 如果得到的值比z小,说明正确的值在右边,所以增大left的值
            elif tmp < z:
                left += 1
            # 相等就加到结果中,并且同时增大和减少left,right
            else:
                ans.append([left, right])
                left += 1
                right -= 1
        return ans
