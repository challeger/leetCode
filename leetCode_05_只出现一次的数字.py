"""
day: 2020-08-10
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x21ib6/
题目名: 只出现一次的数字
题目描述: 给定一个非空整数数组,除了某个元素只出现一次,其余元素均出现两次,找出那个只出现了一次的元素
示例:
    给定nums = [1, 2, 2, 1, 5, 4, 4]
    得到结果 5
思路:
1. 使用集合去重:
    去重之后,集合的和乘以2,得到的结果正好是数组的和乘以2 + 单身狗元素
2. 使用异或:
    若x = y, 则 x ^ y = 0, 所以遍历数组全部异或,得到的结果就是单身狗元素
"""


class Solution(object):
    @staticmethod
    def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 集合去重求和
        # return sum(set(nums)) * 2 - sum(nums)

        # 异或
        single = 0
        for i in nums:
            single ^= i
        return single


if __name__ == "__main__":
    nums = [1, 2, 2, 1, 5, 4, 4]
    print(Solution.singleNumber(nums))
