"""
day: 2020-08-15
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnq4km/
题目名: 打家劫舍
题目描述: 你是一个专业的小偷,计划偷窃沿街的房屋,影响你偷窃的唯一制约因素就是相邻的房屋装有
相互连通的放到系统,若两间相邻的房屋在同一晚上被小偷闯入,系统会自动报警.
给定一个代表每个房屋存放金额的非负整数数组,计算你不触动警报装置情况下的最大金额
示例:
    输入: [1, 2, 3, 1]
    输出: 4 1+3
    输入:[2, 7, 9, 3, 1]
    输出: 12 2+9+1
思路:
1. 动态规划
    对于在第n家的状态,有两种选择
        偷: 那么前面的第n-1家不能偷,偷窃的总金额是 前面k-2家的最高总金额+k的金额
        不偷: 那么偷窃的总金额为前面k-1家的最高总金额
    可以列出状态转移方程:
        dp[i] = max(dp[i-2]+nums[i], dp[i-1])
    最终的答案即dp[n-1]
"""


class Solution:
    def rob(self, nums: list) -> int:
        if nums:
            first = 0
            second = nums[0]
            for i in range(1, len(nums)):
                second, first = max(second, first+nums[i]), second
            return second
        return 0


if __name__ == "__main__":
    s = Solution()
    test = [1]
    print(s.rob(test))
