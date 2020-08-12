"""
day: 2020-08-12
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn96us/
题目名: 有效的字母异位词
题目描述: 给定两个字符串s和t, 编写一个函数来判断t是否是s的字母异位词
示例:
    输入: s='anagram', t='nagaram'
    输出: true

    输入: s='cat', t='rat'
    输出: false
思路:
1. 利用python内置的Counter
2. 自己计算出现次数
"""


class Solution:
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # from collections import Counter
        # return Counter(s) == Counter(t)
        foo = {}
        for index in range(len(s)):
            foo[s[index]] = foo.get(s[index], 0) + 1
            foo[t[index]] = foo.get(t[index], 0) - 1
        for i in foo.values():
            if i != 0:
                return False
        return True


if __name__ == "__main__":
    s = 'aba'
    t = 'baa'
    print(Solution.isAnagram(s, t))
