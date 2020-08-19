"""
day: 2020-08-19
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xv67o6/
题目名: 子集
题目描述: 给定一组不含重复元素的整数数组nums,返回该数组所有可能的子集
示例:
    输入: [1, 2, 3]
    输出:
    [
        [3],
        [1],
        [2],
        [1,2,3],
        [1,3],
        [2,3],
        [1,2],
        []
    ]
思路:
1. 回溯
与全排列思路大致相同,但添加一个限定条件,剩余的数字中,必须大于已排列数字的最后一位,才能进行排列
当已排列的数字长度为0则都可以进行排列.每次排列时先将上一次排列的结果添加到res中.
2. 在已有的子集上追加
    在已有的子集上追加当前数字,然后将得到的list[list[int]]追加到res中.
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res.extend([curr+[num] for curr in res])
        return res
        # def backtrack(first=0):
        #     res.append(nums[:first])
        #     for i in range(first, len(nums)):
        #         if first == 0 or nums[first-1] < nums[i]:
        #             nums[first], nums[i] = nums[i], nums[first]
        #             backtrack(first+1)
        #             nums[first], nums[i] = nums[i], nums[first]
        # res = []
        # backtrack()
        # return res


if __name__ == "__main__":
    test = [1, 2, 3]
    s = Solution()
    print(s.subsets(test))
