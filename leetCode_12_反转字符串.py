"""
day: 2020-08-12
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnhbqj/
题目名: 反转字符串
题目描述: 给定一个字符数组,原地修改输入数组,将输入的字符串反转过来
示例:
    输入: ['h', 'e', 'l', 'l', 'o']
    输出: ['o', 'l', 'l', 'e', 'h']
思路:
1. 内置函数reverse

2. 双指针替换
    定义一个指向首部的指针left与指向尾部的指针right
    每次循环将两个指针指向的值互换,直到left > right
"""


class Solution(object):
    @staticmethod
    def reverseString(s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # 解法1
        # s.reverse()

        # 解法2
        left = 0
        right = len(s) - 1
        while right > left:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    test = ['h', 'e', 'l', 'l', 'o']
    Solution.reverseString(test)
    print(test)
