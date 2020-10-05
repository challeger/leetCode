"""
day: 2020-10-05
url: https://leetcode-cn.com/problems/4sum/
题目名: 四数之和
给定一个包含 n 个整数的数组 nums 和一个目标值 target,判断 nums 中是否存在四个元素 a,b,c 和 d
使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组.
注意：

答案中不可以包含重复的四元组.

思路:
    用字典来记录每两个数字之和得到的值,对应的数字组合.
    然后两两遍历数组,判断 差值是否在字典中,并且还要判断是否用了同一个元素
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        hashmap = dict()  # 用来记录两数之和对应的组合
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                hashmap.setdefault(nums[i]+nums[j], []).append((i, j))
        res = set()  # 记录结果
        for i in range(n):
            for j in range(i+1, n):
                # 如果有对应的差值
                for x, y in hashmap.get(target-nums[i]-nums[j], []):
                    temp = {i, j, x, y}
                    # 并且没有重复的元素
                    if len(temp) == 4:
                        # 那么就将该组合添加到集合中
                        res.add(tuple(sorted(nums[t] for t in temp)))
        # 最终返回一个列表
        return list(res)
