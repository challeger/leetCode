"""
day: 2020-08-20
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvg25c/
题目名: 颜色分类
题目描述: 给定一个包含红色,白色和蓝色,一共n个元素的数组,原地对它们进行排序,使得相同颜色的元素相邻,并按照红色
白色,蓝色顺序排列
0:红色, 1:白色, 2:蓝色
示例:
    输入: [2, 0, 2, 1, 1, 0]
    输出: [0, 0, 1, 1, 2, 2]
思路:
    定义三个指针,一个指向0的最右边界next_red,一个指向2的最左边界next_blue,一个指向当前元素idx
    nums[idx]=2时,将nums[idx]与nums[next_blue]互换位置,next_blue -= 1,idx保持不变
    nums[idx]=0时,将nums[idx]与nums[next_red]互换位置,idx与next_red都右移一位
    nums[idx]=1时,idx右移一位
    直到idx指向2的最左边界.
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        next_red_idx = 0
        n = len(nums)
        next_blue_idx = n - 1
        while idx <= next_blue_idx:
            if nums[idx] == 0:
                nums[idx], nums[next_red_idx] = nums[next_red_idx], nums[idx]
                next_red_idx += 1
                idx += 1
            elif nums[idx] == 2:
                nums[idx], nums[next_blue_idx] = nums[next_blue_idx], nums[idx]
                next_blue_idx -= 1
            else:
                idx += 1


if __name__ == "__main__":
    test = [0, 1, 2, 0]
    s = Solution()
    s.sortColors(test)
    print(test)
