"""
day: 2020-10-07
url: https://leetcode-cn.com/problems/sort-colors/
题目名: 颜色分类
给定一个包含红色,白色和蓝色,一共n个元素的数组,原地对它们进行排序
使得相同颜色的元素相邻,并按照红色,白色和蓝色的顺序排列
0, 1, 2 分别代表红色,白色和蓝色
思路:
    分别排序左边的红色数组与右边的蓝色数组,排序完成后,中间的必然都是白色数组.
    定义next_red来表示下一个红色元素应该在的位置,初始值应该为0
    定义next_blue来表示下一个蓝色元素应该在的位置,初始值应该为n-1
    定义一个指针idx来遍历数组
    当nums[idx] 为 0时,就与next_red交换位置,然后两个指针都右移一位(因为idx >= next_red),所以
    交换时next_red指向的元素必然是白色.
    当nums[idx] 为 2时,就与next_blue交换位置,然后next_blue左移一位,注意idx不能动,因为无法保证
    next_blue之前指向的元素是否需要交换
    当idx > next_blue时,那么就交换完成了,可以结束循环.
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        n = len(nums)
        next_red = 0
        next_blue = n - 1
        while idx < n:
            if idx > next_blue:
                break
            if nums[idx] == 0:
                nums[idx], nums[next_red] = nums[next_red], nums[idx]
                next_red += 1
                idx += 1
            elif nums[idx] == 2:
                nums[idx], nums[next_blue] = nums[next_blue], nums[idx]
                next_blue -= 1
            else:
                idx += 1
