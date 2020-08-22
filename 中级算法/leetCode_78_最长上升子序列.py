"""
day: 2020-08-22
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xwhvq3/
题目名: 最长上升子序列
题目描述: 给定一个无序的整数数组,找到其最长上升子序列的长度
示例:
    输入: [10, 9, 2, 5, 3, 7, 101, 18]
    输出: 4
思路:
1.动态规划
    每次去遍历当前数字的前面的数组,如果比当前数字小,就取max(dp[j]+1, dp[i])
    若剩下的数字已经不可能超过当前的最长子序列长度,就退出循环
2.贪心+二分查找
    维护一个数组d,d[i]表示在长度为i+1的子序列中,所有子序列结尾的最小值
    遍历nums,若nums比d[-1]大,则直接添加到d中,否则通过二分查找,找到d中
    第1个比num大的数,然后替换掉他
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # if not n:
        #     return 0
        # dp = [1 for _ in range(n)]
        # max_length = 1
        # for i in range(1, n):
        #     for j in range(i-1, -1, -1):
        #         # 如果还未遍历的数字长度,小于目前的子序列长度了
        #         # 那么已经没有遍历的必要了,因为无论如何都不会增加最长长度
        #         if j+1 < dp[i]:
        #             break
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[j]+1, dp[i])
        #             max_length = max(dp[i], max_length)
        # return max_length

        # d[i]表示长度i+1的子序列中,所有上升子序列中结尾的最小值
        d = []
        for n in nums:
            # 如果当前遍历的数字比上升子序列中的最后一位大,
            # 那么直接添加到子序列后面
            if not d or n > d[-1]:
                d.append(n)
            else:
                # 否则进行二分查找,找到第1个比n大的数
                left, right = 0, len(d) - 1
                while left < right:
                    # 选左中位,最后left必然指向第1个比n大的数
                    mid = (left + right) >> 1
                    if d[mid] >= n:
                        right = mid
                    else:
                        left = mid + 1
                d[left] = n
        return len(d)


if __name__ == "__main__":
    test = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    s = Solution()
    print(s.lengthOfLIS(test))
