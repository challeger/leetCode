"""
day: 2020-08-20
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xv4hjg/
题目名: 寻找峰值
题目描述: 峰值元素是指其值大于左右相邻值的元素.
给定一个输入数组nums,其中nums[i]≠nums[i+1],找到峰值元素并返回其索引
数组可能包含读个峰值,在这种情况下,返回任何一个峰值的索引即可
示例:
    输入: nums=[1, 2, 3, 1]
    输出: 2
    输入: nums = [1, 2, 1, 3, 5, 6, 4]
    输出: 1 或 5
思路:
二分查找,每次选取中间点mid,判断它与右侧元素的关系
若mid<mid+1,说明中间点在上升的坡上,那么峰值就在[mid+1, right]中
否则说明中间点在下降的坡上,那么峰值就在[left, mid]中
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    test = [1, 2, 3, 1]
    s = Solution()
    print(s.findPeakElement(test))
