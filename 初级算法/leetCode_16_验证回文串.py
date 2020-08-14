"""
day: 2020-08-12
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xne8id/
题目名: 验证回文串
题目描述: 给定一个字符串,验证它是否为回文串,只考虑字母和数字字符, 忽略字母的大小写
示例:
    输入: "A man, a plan, a canal: Panama"
    输出: true

    输入: "race a car"
    输出: false
思路:
1. 筛选出字符串中的字母与数字,组成一个新的字符串,判断字符串反转后是否等于字符串
2. 使用双指针,分别从左右开始遍历,跳过非字母和数字字符的字符,将两个指针的值进行对比,不相同返回false
"""


class Solution:
    @staticmethod
    def isPalindrome(s: str) -> bool:
        # foo = ''.join(ch.lower() for ch in s if ch.isalnum())
        # return foo == foo[::-1]

        length = len(s)
        left, right = 0, length-1
        while right > left:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    test = 'A man, a plan, a canal: Panama'
    print(Solution.isPalindrome(test))
