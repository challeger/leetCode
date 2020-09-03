"""
day: 2020-09-03
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xd3jrg/
题目名: 最大数
给定一组非负整数,重新排列它们的顺序使之组成一个最大的整数

输出结果可能很大,请返回字符串而不是整数
示例:
    输入: [10, 2]
    输出: 210
    输入: [3, 30, 34, 5, 9]
    输出: 9534330

思路:
为了输出最大的数,我们只要保证对于列表中的每一个字符串i,都有nums[i]+nums[i-1] > nums[i-1]+nums[i]
这样拼接起来后得到的字符串就是最大数
算法的证明: 
传递性: cmp(c1, c2) and cmp(c2, c3) -> cmp(c1, c3)
假设存在某个最大序列,他中间有两个字符串,存在nums[i]+nums[i-1]<nums[i-1]+nums[i],那么将这对字符串
顺序反过来后,并不会影响到其他的字符串,并且对于这两个字符串,他们交换后得到的值应该是严格大于之前的值的,
那么该序列就不是最优序列.
"""
from typing import List


class LargerNumber(str):
    # 重写比较大小的方法,设为两个字符串排列顺序的比较
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 将重写的方法作为比较的key
        nums = sorted(map(str, nums), key=LargerNumber)
        # 因为用例中有['0', '0']的存在,所以需要特判
        return '0' if nums[0] == '0' else ''.join(nums)


if __name__ == "__main__":
    test = [0]
    s = Solution()
    print(s.largestNumber(test))
