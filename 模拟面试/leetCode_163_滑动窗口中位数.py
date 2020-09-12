"""
day: 2020-09-12
url: https://leetcode-cn.com/problems/sliding-window-median/submissions/
题目名: 滑动窗口中位数
给你一个数组 nums，有一个大小为 k 的窗口从最左端滑动到最右端。
窗口中有 k 个数，每次窗口向右移动 1 位。
你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组
思路:
1.二分查找
    维护一个有序数组,每次有新元素进窗口,就用二分查找将其插入数组中,
    如果窗口的大小达到了最大值,那么就找到最左边的元素在数组中的位置,将其弹出.
"""
from typing import List
import bisect


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        arr = []
        left = 0
        res = []
        for right in range(len(nums)):
            # 二分插入维护一个有序数组
            bisect.insort(arr, nums[right])
            # 如果超过了窗口的范围,就二分查找找到要弹出的数的位置,然后删除
            while len(arr) > k:
                arr.pop(bisect.bisect_left(arr, nums[left]))
                left += 1
            if len(arr) == k:
                # 用 // 可以免除奇偶数的影响,如果是奇数,那么两个相加的都是它自己
                # 如果是偶数,那么就是中间的左右两个数
                res.append((arr[k // 2] + arr[(k - 1) // 2]) / 2.0)
        return res
