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

2. 记录数字出现的次序
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
        nums.sort()
        for i in nums:
            num_count[i] += 1
        for key, value in enumerate(num_count):
            if key >= 0 and value < 3:
                break
            if key == 0 and value > 2:
                res.append([0, 0, 0])
            elif value > 1:
                if -2 * key in num_count:
                    res.append([value, value, -2*value])
            else:
                y_z = -value
                for y in num_count.keys():
                    z = y_z - y
                    if z < y:
                        break
                    if z in num_count.keys() and z != y:
                        res.append([value, y, z])
        return res


if __name__ == "__main__":
    s = Solution()
    test = [-1, 0, 1, 2, -1, -4]
    print(s.threeSum(test))
