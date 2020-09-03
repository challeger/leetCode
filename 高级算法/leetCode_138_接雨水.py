"""
day: 2020-09-03
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xdkk5t/
题目名: 接雨水
给定n个非负整数表示每个宽度为1的柱子的高度图,计算按此排列的柱子,下雨之后能接多少雨水

示例:
    输入: [0,1,0,2,1,0,1,3,2,1,2,1]
    输出: 6
思路:
1. 单调递减栈
    从左到右遍历数组,当遇到比栈顶小的元素时,说明还无法形成低洼,将其入栈,
    若遇到了比栈顶元素高的柱子,那么将栈顶元素top弹出,让当前的栈顶元素与柱子形成一个边界,
    取他们之间较小的一个作为边界的高度,减去top,就是当前的桶的高度,宽度就是当前柱子的索引-
    当前栈顶元素的索引-1
2. 双指针
    定义两个指针left与right分别从数组左边与右边开始遍历,
    当height[left] < height[right]时,那么height[right]就可以作为当前的left的右边界,而当前
    柱子的积水高度,应该由左边的最高的柱子来决定.当height[left]<height[right]时,当前的left_max必然是小于height[right]的.
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 双指针
        left, right = 0, len(height)-1
        ans = 0
        # 记录当前左边的最高边与当前右边的最高边
        left_max = right_max = 0
        # 对于当前指针存储雨水的格数,应该是由它的最低边界决定的
        # left与right总有一个指针指向当前遍历过的柱子的最高点
        while left < right:
            # 当我们左指针指向的柱子高度小于右指针指向的柱子高度时
            # 那么当前柱子的高度应该依赖于当前左边的最高高度
            if height[left] < height[right]:
                # 首先判断当前柱子的高度是否比之前左边的最高柱子高
                # 若是,则将左边最高高度设为当前柱子的高度
                if height[left] >= left_max:
                    left_max = height[left]
                # 然后判断积水是多少
                ans += (left_max - height[left])
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                ans += (right_max - height[right])
                right -= 1
        return ans

    def trap_stack(self, height: List[int]) -> int:
        stack = []
        i = res = 0
        while i < len(height):
            # 如果当前高度比栈顶元素高,那么说明可能形成了低洼,可以计算积水量
            # 一直循环计算到栈顶比当前元素高,或者栈中没有元素了.
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                # 如果弹出栈顶元素后栈为空,那么说明没有边界来形成低洼,直接退出
                if not stack:
                    break
                # 低洼的宽度
                width = i - stack[-1] - 1
                # 低洼的高度
                min_height = min(height[i], height[stack[-1]]) - height[top]
                res += (min_height * width)
            stack.append(i)
            i += 1
        return res


if __name__ == "__main__":
    test = [8, 5, 0, 4, 6]
    s = Solution()
    print(s.trap(test))
