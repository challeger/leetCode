"""
day: 2020-08-16
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvpj16/
题目名: 三数之和
题目描述: 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素a,b,c
使得 a+b+c=0 请你找出所有满足条件且不重复的三元组
示例:
    输入: [-1, 0, 1, 2, -1, -4]
    输出: [
        [-1, 0, 1],
        [-1, -1, 2]
    ]
思路:
1. 排序+两重循环+指针
先将数组排序,当我们在循环时,若本次枚举的变量与上一次枚举的变量相等,则直接跳过本次循环
若我们在第一层循环枚举的变量a大于0,则直接退出循环.在第二重循环中,我们定义两个指针,分别从头与尾
开始,当头指针b指向的变量与尾指针c指向的变量>-a时,将尾指针左移一位,直到b == c或者 两个指针的值的和
<=-a时,进行比较,若b==c,随着b的增加,数组中不可能存在c满足条件,所以直接跳出本次循环,否则看值是否为0

2. 记录数字出现的次数
使用字典记录数组中数字出现的次数,在遍历数组时我们会遇到三种情况
1. key为0且value>2:
    将[0, 0, 0]添加到res中
2. value>1且key*-2存在于字典中:
    将[key, key, key*-2]添加到res中
3. 正常情况:
    对于我们当前状况的答案,三个数字的关系应该是
    x < y < z, y + z = -x, 所以z的最小值应该是(-x//2+1)
    我们定义一个z的指针,从右侧开始,一直移动到它指向的值小于等于z的最小值,
    在移动过程中,y=-x-z,我们判断这个y是否>x且在字典中,若是则将[x, y, z]存入结果中
"""


class Solution:
    def threeSum(self, nums: list) -> list:
        # n = len(nums)
        # foo = sorted(nums)
        # result = []
        # for a in range(n):
        #     # 若和上一次枚举的变量相同,则直接开始下一轮循环
        #     if a > 0 and foo[a] == foo[a-1]:
        #         continue
        #     elif foo[a] > 0:
        #         break
        #     c = n - 1
        #     target = -foo[a]
        #     for b in range(a+1, n):
        #         # 若和上一次枚举的变量相同,则直接开始下一轮循环
        #         if b > a+1 and foo[b] == foo[b-1]:
        #             continue
        #         while b < c and foo[b] + foo[c] > target:
        #             c -= 1
        #         if b == c:
        #             break
        #         if foo[b] + foo[c] == target:
        #             result.append([foo[a], foo[b], foo[c]])
        # return result
        from collections import defaultdict
        res = []
        num_count = defaultdict(int)
        for i in nums:
            num_count[i] += 1
        nums = sorted(num_count)
        for idx, x in enumerate(nums):
            if x == 0 and num_count[x] > 2:
                res.append([0, 0, 0])
            elif x != 0 and num_count[x] > 1:
                if x * -2 in num_count:
                    res.append([x, x, x * -2])
            if x < 0:
                y_and_z = -x
                z_min = -x // 2
                z_idx = len(nums) - 1
                while nums[z_idx] > z_min:
                    y = y_and_z - nums[z_idx]
                    if y > x and y < nums[z_idx] and y in num_count:
                        res.append([x, y, nums[z_idx]])
                    z_idx -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    test = [1, 1, -2]
    print(s.threeSum(test))
