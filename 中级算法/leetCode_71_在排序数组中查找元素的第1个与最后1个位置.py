"""
day: 2020-08-20
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xv4bbv/
题目名: 在排序数组中查找元素的第1个与最后1个位置
题目描述: 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。
示例:
    输入: nums = [5,7,7,8,8,10], target = 8
    输出: [3,4]
    输入: nums = [5,7,7,8,8,10], target = 6
    输出: [-1,-1]
思路:
两次二分查找

第一次二分查找,找左边界,当mid >= target时,区间要向左收缩,直到left=right,此时left与right指向就是左边界,
因为right = mid
第二次二分查找,找右边界,当mid <= target时,区间要向右收缩,直到left=right,而此时left与right指向的值
应该是右边界的下一个值,因为left = mid + 1
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def helper(is_left):
            left = 0
            right = size
            while left < right:
                mid = (left+right) // 2
                if nums[mid] > target or (is_left and target == nums[mid]):
                    right = mid
                else:
                    left = mid + 1
            return left
        # while left <= right:
        #     if res[0] == -1:
        #         if nums[left] == target:
        #             res[0] = left
        #         else:
        #             left += 1
        #     if res[1] == -1:
        #         if nums[right] == target:
        #             res[1] = right
        #         else:
        #             right -= 1
        #     if res[0] != -1 and res[1] != -1:
        #         break
        size = len(nums)
        left_idx = helper(True)
        if left_idx == size or nums[left_idx] != target:
            return [-1, -1]
        return [left_idx, helper(False)-1]


if __name__ == "__main__":
    test = [5, 7, 7, 8, 8, 10]
    num = 8
    s = Solution()
    print(s.searchRange(test, num))
