"""
day: 2020-08-15
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn4n7c/
题目名: 罗马数字转整数
题目描述: 罗马数字包含七种字符: I, V, X, L, C, D, M
I->1 V->5 X->10 L->50 C->100 D->500 M->1000
示例:
    输入: 'III'
    输出: 3
    输入: 'IV'
    输出: 4
思路:
    用一个变量记录上一个字母的值,若当前字母的值大于上一个字母的值,则需要从结果中减去上一个字母的值
    否则加上上一个字母的值,遍历完成后需要加上最后一个字母的值.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        prev = hashmap[s[0]]
        for i in range(1, len(s)):
            num = hashmap[s[i]]
            if num > prev:
                result -= prev
            else:
                result += prev
            prev = num
        result += prev
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt('MCMXCIV'))
