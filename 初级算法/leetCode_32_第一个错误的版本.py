"""
day: 2020-08-14
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnto1s/
题目名: 第一个错误的版本
题目描述: 假设你有n个版本[1, 2, 3, ..., n], 你想找出导致之后所有版本出错的第一个错误的版本
通过调用isBadVersion(version)接口来判断版本号version是否在单元测试中出错,最终返回第一个出错的版本
示例:
    输入:
    n = 5, 且version = 4是第一个错误的版本
    返回:
    4
思路:
1. 二分查找
    mid = (left + right) // 2
    如果mid不是错误的版本,那么left = mid + 1
    如果mid是错误的版本,那么right = mid
"""


def isBadVersion(version):
    return version >= 4


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1
        return left


if __name__ == "__main__":
    s = Solution()
    print(s.firstBadVersion(5))
