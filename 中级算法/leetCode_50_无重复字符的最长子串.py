"""
day: 2020-08-17
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xv2kgi/
题目名: 无重复字符的最长子串
题目描述: 给定一个字符串,请你找出其中不含有重复字符的 最长子串 的长度。
示例:
    输入: "abcabcbb"
    输出: 3
    解释: 因为无重复字符的最长子串是 "abc",所以其长度为 3

    输入: "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b",所以其长度为 1
思路:
定义一个指针k,指向无重复字符串的首字符的前一个位置
定义一个字典记录各个字母出现的位置,若已经记录过,则将k移动到记录的位置
每次循环都执行 res = max(res, i-k)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k, res, c_dict = -1, 0, {}
        for i, c in enumerate(s):
            if c in c_dict and c_dict[c] > k:
                k = c_dict[c]
                c_dict[c] = i
            else:
                c_dict[c] = i
                res = max(res, i-k)
        return res


if __name__ == "__main__":
    s = Solution()
    test = "pwwkew"
    print(s.lengthOfLongestSubstring(test))
