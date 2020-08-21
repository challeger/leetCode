"""
day: 2020-08-21
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvb8zs/
题目名: 跳跃游戏
题目描述: 给定一个非负整数数组,你最初处于数组的第一个位置
数组中的每个元素代表你在该位置可以跳跃的最大长度
判断你是否能够到达最后一个位置
示例:
    输入: [2, 3, 1, 1, 4]
    输出: true
    说明: 我们可以先跳1步,从位置0到达位置1,然后再从位置1跳3步到达最后一个位置
    输入: [3, 2, 1, 0, 4]
    输出: false
    说明: 无论怎样跳,都会到达索引为3的位置,该位置无法进行跳跃,所以永远不可能到达下一个位置
思路:
    贪心算法,用一个值max_right记录当前能跳跃到的最远的地方,
    若当前遍历的点i在这个范围内,那么max_right = max(max_right, nums[i]+i)
    否则说明已经无法到达终点,直接返回false
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, max_right = len(nums), 0
        for i in range(n):
            if i <= max_right:
                max_right = max(max_right, i + nums[i])
                if max_right >= n-1:
                    return True
            else:
                return False


if __name__ == "__main__":
    test = [3, 0, 2, 2, 0, 0, 1]
    s = Solution()
    print(s.canJump(test))
