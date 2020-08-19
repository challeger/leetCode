"""
day: 2020-08-19
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvqup5/
题目名: 全排列
题目描述: 给定一个没有重复数字的序列,返回其所有可能的全排列.
示例:
    输入: [1, 2, 3]
    输出:
    [
        [1,2,3],
        [1,3,2],
        [2,1,3],
        [2,3,1],
        [3,1,2],
        [3,2,1]
    ]
思路:
假设用一个数组res来存放排列好的数字,一个集合used存放使用过的数字,
我们每次排列时,循环遍历nums,判断当前数字是否在used中,若不在,则将
数字添加到res的末尾与used中,然后将res与used作为变量进行下一次排列,
最后进行res.pop()与used.remove()进行状态回溯, 当res的长度等于nums的长度时,
说明排列出了一种结果.

我们也可以只使用O(1)的额外空间来实现,那就是把nums分开来,以一个分界点first,这个分界点之前
的是排列好的数字,在这个分界点之后的是待排列的数字,每次我们遍历nums[first:],然后将里面的数字
与nums[first]互换位置,然后将得到新first作为参数进行下一次排列.当这一次的排列全部完成,再将nums[first]
与当前的数字互换位置,也就是状态恢复.
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            # 如果开始的位置与长度相等,说明已经得出一种排列结果
            if first == n:
                res.append(nums[:])
            # 将nums分成两半,nums[:first]代表已经排列好的组合,
            # nums[first:]代表待排列的数字,遍历nums[first:],依次
            # 将里面的数字排列到nums[first]上
            for i in range(first, n):
                # 进行排列
                nums[first], nums[i] = nums[i], nums[first]
                # 排列下一个位
                backtrack(first + 1)
                # 将数组还原到未排列时
                nums[first], nums[i] = nums[i], nums[first]
        n = len(nums)
        res = []
        backtrack()
        return res


if __name__ == "__main__":
    test = [1, 2, 3]
    s = Solution()
    print(s.permute(test))
