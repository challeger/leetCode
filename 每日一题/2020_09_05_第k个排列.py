"""
day: 2020-09-05
url: https://leetcode-cn.com/problems/permutation-sequence/
题目名: 第k个排列
给出集合[1, 2, 3, ..., n], 其所有元素共有n!种排列.
按大小顺序列出所有排列情况,并一一标记,当n=3时排列如下:
    1. 123
    2. 132
    3. 213
    4. 231
    5. 312
    6. 321
给定n和k,返回第k个排列
思路:

"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 未用数字的数组
        nums = []
        # 当前的阶乘
        factorial = 1
        # 首先将数全部加入nums中,并计算当前的阶乘
        for i in range(1, n+1):
            nums.append(str(i))
            factorial *= i
        res = ""
        # 第k个排列,在结果中的索引是k-1
        k -= 1
        while nums:
            # 对于4的阶乘,他可以由四个数字开头,每个数字开头组成的数组的长度是 4! / 4
            factorial = factorial // n
            # 计算第k个排列由哪个数字开头..
            temp = k // factorial
            # 那就把这个数字添加到结果中,并从数组中删除该数字
            res += nums[temp]
            nums.pop(temp)
            # 接着找下一个数字
            k %= factorial
            n -= 1
        return res


if __name__ == "__main__":
    test1 = 4
    test2 = 4
    s = Solution()
    print(s.getPermutation(test1, test2))
