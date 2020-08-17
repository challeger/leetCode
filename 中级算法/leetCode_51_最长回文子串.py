"""
day: 2020-08-17
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvn3ke/
题目名: 最长回文子串
题目描述: 给定一个字符串s,找到s中最长的回文子串,假设s的最大长度为1000
示例:
    输入: "babad"
    输出: 'bab' or 'aba'
    解释: 因为无重复字符的最长子串是 "abc",所以其长度为 3

    输入: 'cbbd'
    输出: 'bb'
思路:
1. 双指针
    左指针每次遍历从0开始,右指针从尾部开始,每次遍历左移一位,然后使用切片
    判断范围内的字符串是否为回文,是则与res进行对比,取较长的字符串.
    若是回文且左指针指向0或1,代表之后的字符串中的回文长度不可能超过当前的回文,
    所以直接退出.
2. 动态规划
    对于一个回文串来说,若去掉它的头尾,它仍然是一个回文串,我们用s[i:j]来表示
    s从i到j的字符串,它会有两种状态,true(是回文串)或false(不是回文串)
    s[i:j]是回文串的前提是s[i+1:j-1]是回文串,且s[i] == s[j],i<=j
3. 中心扩展算法(动态规划优化)
    所有的状态在转移时的可能性都是唯一的,我们可以枚举所有边界情况,然后从边界情况开始
    向两边扩散,如从s[i+1, j-1]扩散到s[i, j],直到s[i]!=s[j]
4. Manacher算法
    我们记录当前扩散到的最右边的长度max_right,以及当时扩散的中心点center,
    那么在之后的指针i在max_right的范围内移动时,我们可以根据i关于center的对称点
    mirror,直接计算出i的最大扩散步长.
    当p[mirror] < max_right-i时,因为mirror与i是关于center是对称的,而且center是
    一个回文子串的中心点,所以p[i] = p[mirror],当p[mirror] > max_right-i时,i
    与mirror只能在center为中心点的回文子串中对称,超过了就不能保证字符相等,所以
    p[i] = max_right-i, 所以核心算法语句就是 p[i] = min(p[mirror], max_right-i)
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 暴力解
        # def is_palindrome(string):
        #     return string == string[::-1]
        # if not s:
        #     return ''
        # left, right, res = 0, len(s), s[0]
        # while left < right:
        #     while not is_palindrome(s[left:right]):
        #         left += 1
        #     res = res if len(res) > right-left else s[left:right]
        #     if left <= 1:
        #         break
        #     left = 0
        #     right -= 1
        # return res

        # 解法2
        # n = len(s)
        # dp = [[False] * n for _ in range(n)]
        # ans = ''
        # for x in range(n):
        #     for i in range(n):
        #         j = i + x
        #         if j >= n:
        #             break
        #         if x == 0:
        #             dp[i][j] = True
        #         elif x == 1:
        #             dp[i][j] = (s[i] == s[j])
        #         else:
        #             dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
        #         if dp[i][j] and x + 1 > len(ans):
        #             ans = s[i:j+1]
        # return ans

        # 解法3
        # def maxRange(left, right):
        #     while left >= 0 and right < len(s) and s[left] == s[right]:
        #         left -= 1
        #         right += 1
        #     return left + 1, right - 1
        # start, end = 0, 0
        # for i in range(len(s)):
        #     # 以i为中心点
        #     left1, right1 = maxRange(i, i)
        #     # 以i,i+1为中心点
        #     left2, right2 = maxRange(i, i+1)
        #     if right1 - left1 > end - start:
        #         start, end = left1, right1
        #     if right2 - left2 > end - start:
        #         start, end = left2, right2
        # return s[start: end+1]

        # def center_spread(string, center):
        #     size = len(string)
        #     i = center - 1
        #     j = center + 1
        #     step = 0
        #     while i >= 0 and j < size and string[i] == string[j]:
        #         i -= 1
        #         j += 1
        #         step += 1
        #     return step
        # n = len(s)
        # if n < 2:
        #     return s
        # new_s = '#' + '#'.join(s) + '#'
        # new_len = 2 * n + 1
        # max_len = 1
        # start = 0
        # for i in range(new_len):
        #     cur_len = center_spread(new_s, i)
        #     if cur_len > max_len:
        #         max_len = cur_len
        #         start = (i - max_len) // 2
        # return s[start: start + max_len]
        size = len(s)
        if size < 2:
            return s
        new_str = '#' + '#'.join(s) + '#'
        new_len = len(new_str)
        # 数组p记录了扫描过的回文子串的信息
        p = [0] * new_len
        # 得到的回文子串中,能延伸到的最右的位置
        max_right = 0
        # 上述回文子串的中心点
        center = 0

        # 当前遍历的中心最大扩散步数,它的长度就是原始字符串中最回文字符串的长度
        max_len = 1
        # 原始字符串中的最长回文子串的起点位置
        start = 1

        for i in range(new_len):
            if i < max_right:
                # i关于center的对称点
                mirror = 2 * center - i
                # 核心算法
                # 当p[mirror] <= max_right-i时,因为i和mirror都是以center为中心的
                # 回文子串中的一点,它们俩两边的字母在回文子串必然是相同的,所以p[i]=p[mirror]

                # 当p[mirror] > max_right-i时,i和mirror两边的字母只能在回文子串范围内相等
                # 所以p[i]只能等于max_right-i,因为max_right后面的字母不确定是什么.
                p[i] = min(max_right-i, p[mirror])
            # 下一次扩散的起点
            left = i - (1 + p[i])
            right = i + (1 + p[i])

            # 尝试扩散
            while left >= 0 and right < new_len and new_str[left] == new_str[right]:
                p[i] += 1
                left -= 1
                right += 1
            # max_right是遍历过的i中 i+p[i]的最大值
            if i + p[i] > max_right:
                max_right = i + p[i]
                center = i
            # 若本次扩散的长度比之前记录的最长长度长,那么更新最长长度与对应起点
            if p[i] > max_len:
                max_len = p[i]
                start = (i-max_len) // 2
        return s[start: start+max_len]


if __name__ == "__main__":
    test = "cbcdcbedcbc"
    s = Solution()
    print(s.longestPalindrome(test))
