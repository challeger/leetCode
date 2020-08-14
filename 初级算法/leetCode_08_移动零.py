"""
day: 2020-08-11
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2ba4i/
题目名: 移动零
题目描述: 给定一个数组nums,编写一个函数将所有0移动到数组的末尾,同时保持非零元素的相对顺序
示例:
    给定nums = [0, 0, 1, 0, 3, 12]
    得到结果 [1, 3, 12, 0, 0, 0]
思路:
1. 暴力删除添加
    通过nums.count(0)获得数组中0的个数count,然后执行count次remove(0),append(0)操作
2. 双指针替换
    快指针遍历数组,慢指针指向非零数组的尾部
    当快指针指向的值不为0时, 将快指针指向的值与慢指针指向的值互换,两个指针都向右移一位
    当快指针指向的值为0时,快指针向右移一位
    快指针遍历完成,数组也就移动完成了
"""


class Solution(object):
    @staticmethod
    def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # count = nums.count(0)
        # for _ in range(count):
        #     nums.remove(0)
        #     nums.append(0)
        right = 0
        for left in range(len(nums)):
            if nums[left] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                right += 1


if __name__ == "__main__":
    nums = [0, 0, 1, 0, 3, 12]
    Solution.moveZeroes(nums)
    print(nums)
