"""
day: 2020-08-25
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xwgcuv/
题目名: 最长连续序列
题目描述: 给定一个未排序的整数数组,找出最长连续序列的长度.
要求算法的时间复杂度为O(n)
示例:
    输入: [100, 4 ,200, 1, 3, 2]
    输出: 4
思路:
1. 集合
    我们将数组中的数字保存在一个集合中,每次我们遍历一个数字,判断它的num+1是否在集合中
    若存在则继续判断下一个num+1,直到num+1不在集合中..
    对于 1, 2, 3, 4  我们判断2, 3, 4都不会得到最长连续序列,这时应该想办法跳过他们.
    我们可以判断一个数是否是一个序列的开头,也就是,是否存在num-1在集合中,若在则跳过本次循环
2. 字典
    我们定义一个集合,键为数组中的值,值为数组中的值所在连续序列的长度.
    对于一个不在集合中的数num,它的连续序列长度应该是 num-1的连续序列长度+num+1的连续序列长度+1
    所以我们每次循环,先判断num是否在集合中,在则跳过本次判断,否则获取num-1的连续序列长度left
    与num+1的连续序列长度right,那么num的连续序列长度就是left+right+1,更新num-left,num+right
    的值,将num保存在字典中,开始下一次循环
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_streak = 0
        # nums_set = set(nums)
        # for num in nums:
        #     if num-1 not in nums_set:
        #         current_num = num
        #         current_streak = 1
        #         while current_num+1 in nums_set:
        #             current_num += 1
        #             current_streak += 1
        #         max_streak = max(max_streak, current_streak)
        # return max_streak
        nums_set = {}
        for num in nums:
            if num not in nums_set:
                left = nums_set.get(num-1, 0)
                right = nums_set.get(num+1, 0)
                current_length = 1 + left + right
                max_streak = max(max_streak, current_length)

                nums_set[num] = current_length
                nums_set[num-left] = current_length
                nums_set[num+right] = current_length
        return max_streak


if __name__ == "__main__":
    test = [100, 4, 200, 1, 3, 2]
    s = Solution()
    print(s.longestConsecutive(test))
