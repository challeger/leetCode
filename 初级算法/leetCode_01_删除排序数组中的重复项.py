"""
day: 2020-08-10 16:20
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2gy9m/
题目名: 删除排序数组中的重复项
题目描述: 给定一个有序数组,在 原地 删除重复出现的元素,使每个元素只出现一次,最终返回无重复数组的新长度,不能使用额外的数组空间.
示例:
    给定nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    最终结果应该返回新的长度length = 5,通过
    print(nums[:length])
    得到的结果应该是
    [0, 1, 2, 3, 4]

思路:
第一种:
    定义一个指针i,倒序遍历数组,如果nums[i] == nums[i-1],则删除该指针当前指向的元素,即nums.pop(i),
    最终返回len(nums)
    遍历数组需要O(n)的时间复杂度,pop操作也需要O(n)的时间复杂度,所以该解法的时间复杂度为O(n^2)
第二种:
    使用双指针,慢指针 i 从 0 开始,快指针 j 从 1 开始,
    遍历数组,
    因为是有序数组,
    所以当nums[i] != nums[j]时,将i后移一位,并把j的值赋给i指向的元素,这样i前面的数组就是一个不重复有序数组
    否则将j后移一位,最终返回i,就是去重后数组的长度
"""


class Solution(object):
    @staticmethod
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # 解法一:使用while正序遍历
        # i = 0
        # j = 1
        # while j < len(nums):
        #     if nums[i] == nums[j]:
        #         nums.pop(i)
        #     else:
        #         i += 1
        #         j += 1
        # return len(nums)

        # 解法一:使用for倒序遍历
        # for i in range(len(nums)-1, 0, -1):
        #     if nums[i] == nums[i-1]:
        #         nums.pop(i)
        # return len(nums)

        # 解法二:使用双指针
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1


if __name__ == "__main__":
    num = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    length = Solution.removeDuplicates(num)
    print(num[:length], length)
