"""
day: 2020-08-22
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xw99u7/
题目名: 快乐数
题目描述: 编写一个算法来判断一个数n是不是快乐数
快乐数的定义为:对于一个正整数,每一次将该数替换为它每个位置上的数字的平方和,然后重复这个过程
直到这个数变为1,也可能是无限循环但始终变不到1,如果可以变为1,那么这个数就是快乐数
示例:
    输入: 19
    输出: true
    1^2 + 9^2 = 82
    2^2 + 8^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 = 1
思路:
1.记录出现过的数字
    用一个集合来存放出现过的数字,若出现重复的,说明进入了循环,那么返回false
    否则直到出现1.
2.快慢指针
    因为是循环的,所以快指针终将与慢指针相遇,相遇说明进入了循环,返回false
    否则直到出现1,返回true
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            total_sum = 0
            while num > 0:
                num, digit = divmod(num, 10)
                total_sum += digit ** 2
            return total_sum
        # nums = set()
        # while n != 1 and n not in nums:
        #     nums.add(n)
        #     n = get_next(n)
        slow = n
        fast = get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1


if __name__ == "__main__":
    test = 100
    s = Solution()
    print(s.isHappy(test))
