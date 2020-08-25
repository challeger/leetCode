"""
day: 2020-08-25
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xw6oqi/
题目名: 盛最多水的容器
题目描述: 给你n个非负整数a1,a2,...,an,每个数代表坐标中的一个点,(i, ai), 在坐标内画n条垂直线
垂直线i的两个端点分别是(i, ai)和(i, 0),找出其中的两条线,使得它们与x轴共同构成的容器可以容纳最多
的水
示例:
    输入：[1,8,6,2,5,4,8,3,7]
    输出：49
思路:
    双指针,分别指向容数组的左侧与右侧,每次计算它的容积
    然后移动高度较小的指针
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height)-1
        while left < right:
            max_area = max(max_area, min(height[left], height[right])*(right-left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area


if __name__ == "__main__":
    test = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()
    print(s.maxArea(test))
