"""
day: 2020-08-25
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xwkftg/
题目名: 缺失的第一个正数
题目描述: 给你一个未排序的整数数组,请你找出其中没有出现的最小正整数
算法的时间复杂度应该为O(n),并且只能使用常数级别的额外空间
示例:
    输入: [3,4,-1,1]
    输出: 2
    输入: [7,8,9,11,12]
    输出: 1
思路:
1. 哈希
    我们可以将数组作为一个哈希表,它的索引+1为键,它的 是否为正数 为值
    遍历哈希表,第一个值为正数的键,就是我们要找的数.
    所以我们可以分为三步:
    N = len(n)
    1.将数组中所有的非正数 赋值N+1(N+1是必定不在正确的数组中的)
    2.根据数组的值,将这个值-1对应的格子,标记为负数
    3.遍历数组,若当前格子的值是正数,那么当前格子的索引+1就是我们缺失的数字
2. 置换
    对于一个数组[3, 2, 4, 1, 6]
    正确的未缺失数组应该是[1, 2, 3, 4, 5]
    也就是,该数组的第i-1个元素,它的值应该是i
    所以我们第一次遍历数组,如果这个格子的值是有效的索引
    把这个格子的值与它应该在的格子交换值,因为交换后当前格子
    的值可能还可以置换,所以我们应该继续交换该格子..
    若当前格子的值等于它要交换的格子的值,说明出现了重复变量,那就
    直接选择不置换
    然后我们第二次遍历,若当前的d[i] != i+1,那么i+1就是我们的缺失的
    正数
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # n = len(nums)
        # # 将所有非正数标记为N+1
        # for i in range(n):
        #     if nums[i] <= 0:
        #         nums[i] = n + 1

        # # 将nums中所有在[1, n]范围内的数作为索引
        # # 将对应的格子标记为负数
        # for i in range(n):
        #     num = abs(nums[i])
        #     if num <= n:
        #         nums[num-1] = -abs(nums[num-1])

        # # 第一个正数的索引+1,就是第一个未出现的正数
        # for i in range(n):
        #     if nums[i] > 0:
        #         break
        # return i + 1
        n = len(nums)
        for i in range(n):
            # 判断这个数是否是有效的索引,然后将数字放到它应该在的位置
            while 0 < nums[i] <= n and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in range(n):
            if nums[i] != i+1:
                return i + 1
        return n + 1


if __name__ == "__main__":
    test = [1, 2, 2]
    s = Solution()
    print(s.firstMissingPositive(test))
