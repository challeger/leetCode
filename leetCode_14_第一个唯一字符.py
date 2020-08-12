"""
day: 2020-08-12
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn5z8r/
题目名: 字符串中的第一个唯一字符
题目描述: 给定一个字符串,找到它的第一个不重复的字符,并返回它的索引.如果不存在,则返回-1
示例:
    输入: 'leetcode'
    输出: 0

    输入: 'loveleetcode'
    输出: 2
思路:
1. 建立 值->索引 的哈希表
    遍历数组,把值->索引存放到哈希表中,如果有重复值,则把索引置为字符串的长度
    最终返回哈希表中的最小值,若最小值为字符串的长度,则返回-1
2. 建立 值->出现次数 的哈希表
    遍历数组,把每个字符出现的次数保存到哈希表中,然后遍历字符串,如果字符出现的次数
    为1,则返回该字符的索引
"""


class Solution:
    @staticmethod
    def firstUniqChar(s: str) -> int:
        if s == '':
            return -1

        foo = {}
        length = len(s)
        for index, value in enumerate(s):
            if value in foo:
                foo[value] = length
            else:
                foo[value] = index
        result = min(foo.values())
        return result if result < length else -1

        # import collections
        # count = collections.Counter(s)

        # for index, value in enumerate(s):
        #     if count[value] == 1:
        #         return index
        # return -1


if __name__ == "__main__":
    s = 'l'
    print(Solution.firstUniqChar(s))
