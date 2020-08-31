"""
day: 2020-08-31
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xdnx6s/
题目名: 摆动排序II
给定一个无序的数组nums,将它重新排列为num[0] < num[1] > num[2] < num[3]..的顺序
示例:
    输入: nums = [1, 5, 1, 1, 6, 4]
    输出: 可能的答案 [1, 4, 1, 5, 1, 6]
思路:
"""
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        mid = length >> 1
        # 通过快速查找获取数组的中位数
        self.quickSelect(nums, 0, length, mid)

        i = j = 0
        k = length - 1
        # 根据中位数将数组三分
        # 左边是小于中位数的数组,中间是等于中位数的数组,右边是大于中位数的数组
        # 3-way-partition
        while j < k:
            if nums[j] > nums[mid]:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            elif nums[j] < nums[mid]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                j += 1
        mid += length % 2
        tmp1 = nums[:mid]
        tmp2 = nums[mid:]
        # 将两边数组反序组合即可
        # 因为对于中位数之前的数字,它的最大值不会超过中位数
        # 而对于中位数之后的数字,它的最小值不会小于中位数
        # 所以在反序排列后,不会出现55这样的错误解答.
        nums[0::2], nums[1::2] = tmp1[::-1], tmp2[::-1]

    def quickSelect(self, nums, begin, end, n):
        t = nums[end-1]
        # i:下一个待交换的元素 j:遍历数组的指针
        i = j = begin
        # 遍历数组
        while j < end:
            # 对于比基准值小的数,就放到左边
            if nums[j] <= t:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1

        # 如果交换好的元素的长度,大于要查找的元素应该在的位置
        # 那么必定在左边
        if i-1 > n:
            self.quickSelect(nums, begin, i-1, n)
        # 否则在右边
        elif i <= n:
            self.quickSelect(nums, i, end, n)


if __name__ == "__main__":
    test = [5, 3, 1, 2, 6, 7, 8, 5, 5]
    s = Solution()
    s.wiggleSort(test)
    print(test)
