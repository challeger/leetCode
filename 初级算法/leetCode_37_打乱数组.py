"""
day: 2020-08-15
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn6gq1/
题目名: 打乱数组
题目描述: 打乱一个没有重复元素的数组
示例:
    初始化数组
    nums = [1, 2, 3]
    solution = Solution(nums)

    打乱数组[1, 2, 3]并返回结果,任何[1, 2, 3]的排列返回的概率应该相同
    solution.shuffle()

    重设数组到它的初始状态[1, 2, 3]
    solution.reset()
思路:
1. 洗牌
    已经洗好的牌放在nums[:i]中,每次从nums[i:]后面随机挑选一张牌,与nums[i]交换
    位置.
2. random.shuffle -> 打乱一个列表的顺序
"""


class Solution:

    def __init__(self, nums: list):
        self.nums = nums
        self.original = nums[:]

    def reset(self) -> list:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.original[:]
        return self.nums

    def shuffle(self) -> list:
        """
        Returns a random shuffling of the array.
        """
        import random
        # random.shuffle(self.nums)
        for i in range(len(self.nums)):
            swap_idx = random.randrange(i, len(self.nums))
            self.nums[i], self.nums[swap_idx] = self.nums[swap_idx], self.nums[i]
        return self.nums


if __name__ == "__main__":
    s = Solution([1, 2, 3])
    print(s.shuffle())
    print(s.shuffle())
    print(s.shuffle())
    print(s.reset())
