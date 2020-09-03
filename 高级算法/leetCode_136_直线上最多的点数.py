"""
day: 2020-09-03
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xd3jrg/
题目名: 直线上最多的点数
给定一个二维平面,平面上有n个点,求最多有多少个点在同一条直线上.
示例:
    输入: [[1,1],[2,2],[3,3]]
    输出: 3
    输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    输出: 4

思路:
    将斜率作为键,该斜率上点的个数作为值,建立一个哈希表..
    因为会有重复的点,所以在一开始使用Counter进行去重与记录次数
    然后遍历每一个点,对于点i,我们要遍历的应该是从i+1开始的所有点,因为之前的点已经全部讨论过了
    每次遍历都用一个哈希表来记录对于该点的,所有斜率上出现的点的次数,这里用最大公约数来求斜率..
    每次就将点出现的次数加到对应的斜率值上,然后每次遍历完,对比最大值时,需要加上当前点本身出现的次数..
"""
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        from collections import Counter, defaultdict

        # 去除重复的点,并记录每个点出现的次数
        counter = Counter(map(tuple, points))
        # 作为遍历的对象
        list_nums = list(counter)
        length = len(list_nums)
        # 如果长度为1,说明只有一个点,就直接返回该点出现的次数
        if length == 1:
            return counter[list_nums[0]]
        res = 0

        # 辗转相除法求两个数的最大公约数
        def gcd(x, y):
            if y == 0:
                return x
            else:
                return gcd(y, x % y)

        for i in range(length-1):
            # 计算i点与其他点的连线
            slope = defaultdict(int)
            # 从i+1开始,因为i之前的点已经全部讨论过了
            for j in range(i+1, length):
                x = list_nums[j][0] - list_nums[i][0]
                y = list_nums[j][1] - list_nums[i][1]
                # 计算斜率,将其化为最简
                g = gcd(y, x)
                y //= g
                x //= g
                # 将相同斜率的点的出现次数加到斜率对应的值上
                slope[f"{y}/{x}"] += counter[list_nums[j]]
            # 最终计算时还要加上点本身出现的次数
            res = max(res, max(slope.values()) + counter[list_nums[i]])
        return res


if __name__ == "__main__":
    test = [[1, 1], [3, 2], [5, 3], [4, 1], [4, 1], [2, 3], [1, 4]]
    s = Solution()
    print(s.maxPoints(test))
