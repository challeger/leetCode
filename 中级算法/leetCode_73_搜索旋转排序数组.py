"""
day: 2020-08-21
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xv11yj/
题目名: 搜索旋转排序数组
题目描述: 假设按照升序排序的数组在预先未知的某个点上进行了旋转
    例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2]
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1
你的算法时间复杂度必须是 O(log n) 级别
示例:
    输入: nums = [4,5,6,7,0,1,2], target = 0
    输出: 4
思路:
二分查找
    当我们将数组一分为二时,[left, mid]与[mid+1, right]至少有一个部分是有序的
    我们可以通过这个有序的部分,去判断target在哪一个区间中
    若nums[0] <= nums[mid],说明nums[0, mid]是一个有序区间,判断target是否在这个区间中
    若是,则搜索区间向右收缩, 否则搜索区间向左收缩
    若nums[0] > nums[mid],说明nums[mid, -1]是一个有序区间,判断target是否在这个区间中
    若是,则搜索区间向左收缩, 否则搜索区间向右收缩
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # mid左边是有序区间
            if nums[0] <= nums[mid]:
                # 在有序区间中则向右收缩
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                # 否则向左收缩
                else:
                    left = mid + 1
            # mid右边是有序区间
            else:
                # 在右边有序区间中,则向左收缩
                if nums[mid] < target <= nums[-1]:
                    left = mid + 1
                # 否则向右收缩
                else:
                    right = mid - 1
        return -1


if __name__ == "__main__":
    test = [4, 5, 6, 7, 0, 1, 2]
    tar = 0
    s = Solution()
    print(s.search(test, tar))
