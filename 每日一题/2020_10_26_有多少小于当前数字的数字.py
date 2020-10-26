"""
day: 2020-10-26
url: https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number/
题目名: 有多少小于当前数字的数字
给你一个数组 nums,对于其中每个元素 nums[i],请你统计数组中比它小的所有数字的数目.
换而言之,对于每个 nums[i] 你必须计算出有效的 j 的数量,
其中 j 满足 j != i 且 nums[j] < nums[i] .

以数组形式返回答案.

示例:
    输入: nums = [8,1,2,2,3]
    输出: [4,0,1,1,3]
思路:
桶:
    因为题目要求数字范围在0 <= num <= 100, 所以可以建立一个范围在0-100的桶
    然后遍历列表记录每个数字的出现次数
    然后再次遍历,数字的和累加
"""
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count_list = [0] * 101
        for n in nums:
            count_list[n] += 1
        foo = []
        temp = 0
        for n in count_list:
            foo.append(temp)
            temp += n
        return [foo[num] for num in nums]
