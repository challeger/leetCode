"""
day: 2020-10-11
url: https://leetcode-cn.com/problems/partition-equal-subset-sum/
题目名: 分割等和子集
给定一个只包含正整数的非空数组.
是否可以将这个数组分割成两个子集,使得两个子集的元素和相等
思路:
    要判断该数组能否分割为两个子集,只需要判断该数组是否有数字组合可以填满 数组的总和的一半,
    那么剩下的一半 剩余的数字必然是正好填满的.

    我们定义一个二维数组dp[i][j]
    i表示nums的前i个数字, j表示要填满的目标数字
    0 <= i <= len(nums) 0 <= j <= sum // 2
    那么当不选中当前第i个数字时
    dp[i][j] = dp[i-1][j],
    选中当前第i个数字时(需要保证nums[i] <= j):
    dp[i][j] = dp[i-1][j-nums[i]]
    如果在计算过程中,某次dp[i][-1]为True,那么说明已经有组合可以填满 sum // 2了,所以就返回True
    否则返回False
"""
from typing import List


class Solution:
    def canPartition_0(self, nums: List[int]) -> bool:
        total_sum = sum(nums)  # 先计算总和
        if total_sum % 2:  # 如果无法整除,那么是不可能平分的
            return False
        n = len(nums)
        half_sum = total_sum // 2  # 我们只需要计算nums中是否有组合可以填满一半,那么剩下的数字自然可以填满另一半
        # dp[i][j]表示nums从0-i的数字中是否有组合能填满容量为j的背包
        dp = [[False] * (half_sum+1) for _ in range(n)]
        if nums[0] <= half_sum:
            dp[0][nums[0]] = True
        for i in range(n):
            dp[i][0] = True  # 容量为0的背包自然是都能填满的

        for i in range(1, n):
            for j in range(half_sum+1):
                dp[i][j] = dp[i-1][j]  # 代表不选中当前数字
                if nums[i] <= j:
                    dp[i][j] |= dp[i-1][j-nums[i]]  # 代表选中当前数字
                if dp[i][-1]:
                    return True
        return False

    def canPartition_1(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        n = len(nums)
        if total_sum % 2:
            return False  # 如果总和是奇数,那么不可能平分

        half_sum = total_sum // 2
        dp = [False] * (half_sum+1)
        dp[0] = True
        if nums[0] <= half_sum:
            dp[nums[0]] = True

        for i in range(1, n):
            # 从大到小更新的原因是 让上一轮得到的dp[j-nums[i]]不会变
            # 如果从小到大更新的话,会先改变dp[j-nums[i]]的值,影响后续的计算
            for j in range(half_sum, -1, -1):
                if nums[i] <= j:
                    dp[j] |= dp[j-nums[i]]
        return dp[-1]


if __name__ == "__main__":
    foo = [3, 5, 1, 3]
    s = Solution()
    print(s.canPartition(foo))
