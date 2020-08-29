"""
day: 2020-08-29
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xdr7yg/
题目名: 分割回文串
给定一个字符串s,将s分割成一些子串,使每个子串都是回文串
返回s所有可能的分割方案
示例:
    输入: "aab"
    输出: [
        ['aa', 'b'],
        ['a', 'a', 'b']
    ]
思路:
1. 回溯法
    依次遍历字符串,然后进行字符串切片操作,如果切片后的字符串是回文,
    那么将其添加到res列表中,然后从切片的末尾的下一个字符开始继续判断,
    若下一个位置指向了size,说明已经遍历完字符串了,将该结果添加到结果列表中.
    每次切片完的添加操作与深入操作后,需要对res列表进行回溯,即进行res.pop()
2. 优化
    优化判断是否回文串的方法,使用中心扩散+动态规划数组记录从i到j是否是一个字符串
    这样就只需要O(1)的时间复杂度即可知道是否是回文串
"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        size = len(s)
        result = []

        def prePro(left, right):
            nonlocal dp
            # 中心扩散法,记录状态
            while left >= 0 and right < size and s[left] == s[right]:
                dp[left][right] = True
                left -= 1
                right += 1

        def helper(idx, res):
            nonlocal result
            if idx == size:
                result.append(res[:])
            for i in range(idx, size):
                if dp[idx][i]:
                    # 添加切割的字符串到数组中
                    res.append(s[idx:i+1])
                    helper(i+1, res)
                    # 回溯
                    res.pop()

        # 表示从i到j的字符串是否为回文
        dp = [[False]*size for _ in range(size)]
        for i in range(size):
            prePro(i, i)
            prePro(i, i+1)

        helper(0, [])
        return result


if __name__ == "__main__":
    test = "aab"
    s = Solution()
    print(s.partition(test))
