"""
day: 2020-08-19
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xv8ka1/
题目名: 电话号码的数字组合
题目描述: 给定一个仅包含数字2-9的字符串,返回所有它能表示的字母组合.
2:abc, 3:def, 4:ghi, 5:jkl, 6:mno, 7:pqrs, 8:tuv, 9:wxyz
示例:
    输入: '23'
    输出: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
思路:
将目前已经产生的组合,与下一个数字的所有字母进行组合
如果接下来没有数字了,说明已经组合完毕,
如果还有数字,那么继续组合
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(combination, next_digits):
            if not next_digits:
                res.append(combination)
            else:
                for letter in hashmap[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])
        res = []
        if digits:
            hashmap = {
                '2': ('a', 'b', 'c'),
                '3': ('d', 'e', 'f'),
                '4': ('g', 'h', 'i'),
                '5': ('j', 'k', 'l'),
                '6': ('m', 'n', 'o'),
                '7': ('p', 'q', 'r', 's'),
                '8': ('t', 'u', 'v'),
                '9': ('w', 'x', 'y', 'z'),
            }
            backtrack('', digits)
        return res


if __name__ == "__main__":
    test = '234'
    s = Solution()
    print(s.letterCombinations(test))
