"""
day: 2020-08-15
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnbcaj/
题目名: 有效的括号
题目描述: 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    注意空字符串可被认为是有效字符串。
示例:
    输入: '()'
    输出: ture
    输入: '([)]'
    输出: false
    输入: '({})'
    输出: true
思路:
利用哈希映射,以及辅助栈,每次遍历,若是左边括号,则将对应的右边括号添加到栈中
若是右边括号,则进行pop操作,判断pop出来的括号是否等于当前括号,是则继续,否则返回false
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        hashmap = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        result = ['?']
        for c in s:
            if c in hashmap:
                result.append(hashmap[c])
            elif result.pop() != c:
                return False
        return len(result) == 1


if __name__ == "__main__":
    test = ''
    s = Solution()
    print(s.isValid(test))
