"""
day: 2020-11-10
url: https://leetcode-cn.com/problems/next-permutation/
题目名: 下一个排列
实现获取下一个排列的函数,算法需要将给定数字序列重新排列成字典序中
下一个更大的排列
如果不存在下一个更大的排列,则将数字重新排成最小的排列
必须原地修改,只允许使用额外常数空间

示例1:
    1,2,3 -> 1,3,2
    3,2,1 -> 1,2,3

思路:
从右往左找,找到第一个比右边小的数m,那么说明可以变得更大
然后再重新从右往左找,找到第一个比m大的数n,将它们两个交换.
之后再将m原本所在的位置后面的所有数,全部倒序.

如果不能再变大,那么它的数从右往左必然是升序的,所以就直接把所有的数倒过来即可.
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        # 首先找到第一个比右边的数小的数
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # 如果有这样的数,说明可以变大
        if i >= 0:
            j = len(nums) - 1
            # 要尽可能小的变大,所以再找第一个比i大的数
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            # 交换两个数
            nums[i], nums[j] = nums[j], nums[i]

        # 再把i后面的所有数倒序即可
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
