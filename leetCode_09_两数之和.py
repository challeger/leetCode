"""
day: 2020-08-11
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2jrse/
题目名: 两数之和
题目描述: 给定一个整数数组nums和一个目标值target,在该数组中找出和为目标值的那两个整数,并返回数组下标
示例:
    给定nums = [2, 7, 11, 15], target = 9
    得到结果 [0, 1]
思路:
1.
    判断target-nums[i]得到的值是否在nums中,在则返回i以及该值的索引
2. 哈希表
    将数组中每个值最后出现的位置存储在一个字典中,然后遍历数组
    判断target-nums[i]得到的值是否在字典中,在则判断两个值的索引位置是否相等
    不相等则返回两个索引值,相等则继续遍历
"""


class Solution(object):
    @staticmethod
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     value = target - nums[i]
        #     if value in nums[i+1:]:
        #         index = i + 1 + nums[i+1:].index(value)
        #         return [i, index]
        dic = {v: i for i, v in enumerate(nums)}
        for i, v in enumerate(nums):
            value = target - v
            if value in dic and i != dic[value]:
                return i, dic[value]


if __name__ == "__main__":
    nums = [2, 2, 11, 15]
    target = 4
    print(Solution.twoSum(nums, target))
