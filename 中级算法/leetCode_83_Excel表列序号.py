"""
day: 2020-08-23
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xweb76/
题目名: Excel表列序号
题目描述: 给定一个Excel表格中的列名称,返回其相应的列序号
A->1, B->2, C->3, Z->26
AA->27, AB->28
ZY->701
示例:
    输入: A
    输出: 1
    输入: ZY
    输出: 701
思路:
    本质是26进制转换,每进1位就乘26
    所以每次遍历一位,ans = ans * 26 + num
"""


class Solution:
    def titleToNumber(self, s: str) -> int:
        base = ord('@')
        res = 0
        for idx, value in enumerate(s):
            num = ord(value) - base
            res = res * 26 + num
        return res


if __name__ == "__main__":
    test = 'ZY'
    s = Solution()
    print(s.titleToNumber(test))
