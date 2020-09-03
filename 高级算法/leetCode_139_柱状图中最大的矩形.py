"""
day: 2020-09-03
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xdzifs/
题目名: 柱状图中最大的矩形
给定n个非负整数,用来表示柱状图中各个柱子的高度,每个柱子彼此相邻,且宽度为1.
求在该柱状图中,能够勾勒出来的矩阵的最大面积

示例:
    输入: [2,1,5,6,2,3]
    输出: 10
思路:
1. 单调递增栈
    对于本题,我们以某个矩形i为最矮的柱子,它的最大面积应该是,向左扩散到某个比它矮的柱子left,以及向右
    右扩散到某个比它矮的柱子right,那么在left与right之间,能勾勒出的最大矩形的面积应该是
    right-left-1,依次计算每一个柱子,取其中最大的值即可...
    我们可以维护一个单调递增栈,对于栈顶元素i,它前面的所有元素都是比它小的,那么当我们遇到一个柱子
    的高度比栈顶元素小时,那么说明,当前栈顶元素的最大勾勒面积就是
    (当前元素的索引-栈顶元素的下一个元素的索引-1)x栈顶元素的高度.
    所以大概的逻辑就是:
    for i in range(len(heights)):
        # 如果栈顶元素的高度大于当前遍历到的元素,那么就可以计算出栈顶元素的最大勾勒面积
        while stack and heights[i] < heights[stack[-1]]:
            # 弹出栈顶元素,那么弹出后当前栈的栈顶元素,就是top的左边界
            top = stack.pop()
            # 然后计算面积
            (i-stack[-1]-1) * height[top]
            # 再进行比较即可
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        # 增加两个虚节点
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            # 维护一个单调递增栈
            while stack and heights[i] < heights[stack[-1]]:
                top = stack.pop()
                # 因为增加了两个虚节点0,所以不用考虑栈为空的问题,0是必然会一直在栈中的.
                res = max(res, (i-stack[-1]-1)*heights[top])
            stack.append(i)
        return res


if __name__ == "__main__":
    test = [2, 1, 5, 6, 2, 3]
    s = Solution()
    print(s.largestRectangleArea(test))
