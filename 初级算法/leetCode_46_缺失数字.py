"""
day: 2020-08-15
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnj4mt/
题目名: 缺失数字
题目描述: 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
示例:
    输入: [3,0,1]
    输出: 2
    输入: [9,6,4,2,3,5,7,0,1]
    输出: 8
思路:
1. 数学解法
    0+1+2+...+n = (0+n)(n+1)/2 -- 高斯求和
    求出的和-数组的和,得到的就是缺失的数字
2. 异或
    循环len(nums)次,每次将idx与value异或
    比如[3, 0, 1]
    缺失的数字 = 3 ^ (0 ^ 3) ^ (1 ^ 0) ^ (2 ^ 1) = (0 ^ 0) ^ (1 ^ 1) ^ (2) ^ (3 ^ 3)
    =0 ^ 0 ^ 2 ^ 0 = 2
"""


class Solution:
    def missingNumber(self, nums: list) -> int:
        # length = len(nums)
        # sum1 = sum(nums)
        # sum2 = length * (length+1) / 2
        # return int(sum2 - sum1)
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing


if __name__ == "__main__":
    test = [6, 4, 2, 3, 5, 7, 0, 1]
    s = Solution()
    print(s.missingNumber(test))
