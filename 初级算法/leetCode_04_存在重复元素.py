"""
day: 2020-08-10
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x248f5/
题目名: 存在重复元素
题目描述: 给定数组,判断数组中是否存在重复元素,是则返回True,否则返回False
示例:
    给定nums = [1, 2, 3, 4, 5]
    得到结果 false
    给定nums = [1, 2, 3, 1]
    得到结果 True
思路:
1. 利用集合去重:
    将数组转换为集合,然后对比数组与集合之间的长度,不相同说明有重复元素
2. 排序后遍历数组:
    利用列表的sort函数排序,然后遍历数组,重复的元素会相邻
"""


class Solution(object):
    @staticmethod
    def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        return len(nums) > len(set(nums))

        # 排序后遍历,如果有重复的会相邻
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return True
        # return False

        # nt写法
        # nums_set = set()
        # for i in nums:
        #     if i in nums_set:
        #         return True
        #     nums_set.add(i)
        # return False


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(Solution.containsDuplicate(nums))
