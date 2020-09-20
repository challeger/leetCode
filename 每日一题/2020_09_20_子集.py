"""
day: 2020-09-20
url: https://leetcode-cn.com/problems/subsets/
题目名: 子集
给定一组不含重复元素的整数数组nums,返回该数组所有可能的子集(幂集).

说明: 解集不能包含重复的子集
思路:

"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for i in nums:
            res = res + [[i] + num for num in res]
        return res


if __name__ == "__main__":
    test = [1, 2, 3]
    s = Solution()
    print(s.subsets(test))
