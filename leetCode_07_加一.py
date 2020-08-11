"""
day: 2020-08-11
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2cv1c/
题目名: 加一
题目描述: 给给定一个由整数组成的非空数组所表示的非负整数,在该数的基础上加一.
数组首位是数字的最高位,除了整数0之外,整数不会以0开头
示例:
    给定nums1 = [1, 2, 2, 4]
    得到结果 [1, 2, 2, 5]
    给定nums2 = [9, 9, 9]
    得到结果 [1, 0, 0, 0]
思路:
1. 从数组尾部开始遍历
    从尾部开始遍历数组,若+1后的值不为10则退出,否则将当前位置为0,并继续循环
    当最高位+1等于10,则将最高位置为0,并且在数组首部插入1
2. 转换为字符串
    将数组拼接成字符串,转为int类型,然后+1,再转换为数组
"""


class Solution(object):
    @staticmethod
    def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # for i in range(len(digits)-1, -1, -1):
        #     digits[i] += 1
        #     if digits[i] == 10:
        #         digits[i] = 0
        #         if i == 0:
        #             digits.insert(0, 1)
        #     else:
        #         break
        # return digits

        return list(map(int, str(int(''.join(map(str, digits))) + 1)))


if __name__ == "__main__":
    digit = [9, 9, 9, 9]
    print(Solution.plusOne(digit))
