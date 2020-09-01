"""
day: 2020-09-01
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xdwst3/
题目名: 乘积最大子数组
给你一个整数数组nums,请你找出数组中乘积最大的连续子数组(该子数组中至少包含一个数字),并返回
该子数组所对应的乘积
示例:
    输入: [2, 3, -2, 4]
    输出: 6
    输入: [-2, 0, -1]
    输出: 0
思路:
    对于正数来说,我们要求其当前乘积的最大值,应该让它去乘之前数组中的最大值
    对于负数来说,我们要求当前乘积的最大值,应该让它去乘之前数组中的最小值
    所以我们在进行状态转移时,需要计算对于当前数来说,乘积的最大值与最小值.

    那么当nums[i] >= 0时:
        dp[i][0] = max(dp[i-1][0]*nums[i], nums[i])
        dp[i][1] = min(dp[i-1][1]*nums[i], nums[i])
    nums[i] < 0时:
        dp[i][0] = max(dp[i-1][1]*nums[i], nums[i])
        dp[i][1] = min(dp[i-1][0]*nums[i], nums[i])
    内存优化:
        对于nums[i]的状态,我们只需要关注nums[i-1]的状态即可
        所以只需要定义两个变量来分别记录前一个数的最大值与最小值

    表达式优化:
        当nums[i]<0时,那么
            max_last * nums[i] <= min_last * nums[i]
        当nums[i]>=0时,那么
            max_last * nums[i] >= min_last * nums[i]
        所以我们在找最大值时,只要找出这两个乘积的最大值,去和nums[i]进行比较
        找最小值同理,找乘积的最小值即可,也就是
        max_now = max(max(max_last*nums[i], min_last*nums[i]), nums[i])
        min_now = min(min(max_last*nums[i], min_last*nums[i]), nums[i])
        最终再取最大值即可.
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_num = nums[0]
        min_num = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            mx = max_num
            mn = min_num
            # 当nums[i]>=0时,那么此时的最大值应该是max(mx*nums[i], nums[i])
            # 当nums[i]<0时,此时的最大值应该是max(mn*nums[i], nums[i])
            max_num = max(max(mx*nums[i], mn*nums[i]), nums[i])
            # 当nums[i]>=0时,此时的最小值应该是min(mn*nums[i], nums[i])
            # 当nums[i]<0时,此时的最小值应该是min(mx*nums[i], nums[i])
            min_num = min(min(mx*nums[i], mn*nums[i]), nums[i])
            ans = max(max_num, ans)
        return ans


if __name__ == "__main__":
    test = [-1, 3, -2, 4]
    s = Solution()
    print(s.maxProduct(test))
