"""
day: 2020-08-13
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnmav1/
题目名: 最长公共前缀
题目描述: 编写一个函数来查找字符串数组中的最长公共前缀,若不存在,则返回空字符串

示例:
    输入: ["flower", "flow", "flight"]
    输出: "fl"

    输入: ["dog", "racecar", "car"]
    输出: ""

思路:
1. 横向扫描,遍历整个列表,每次遍历一个字符串,用一个临时变量来保存公共前缀,依次对比下去,如果在某次遍历
时,公共前缀变为了'',就可以直接返回''了
2. 纵向扫描,以列表的第一个元素的长度length为基准,循环length次,每次循环比较列表中各个字符串的第i个字符,
如果有与第一个元素的第i个字符不相等的,或者是i已经为某字符串的长度时,公共前缀就是 strs[0][:i],若循环完成
则前缀就是strs[0]
3. 将列表排序,然后直接将第一个字符串与最后一个字符串进行比较,得到的前缀就是最长公共前缀
4. 分治法,利用递归,将列表两两分解,最终将对比获得的前缀进行比较,得到的结果就是最长公共前缀
"""


class Solution:
    @staticmethod
    def longestCommonPrefix(strs: list) -> str:
        # if not strs:
        #     return ''
        # strs = sorted(strs)
        # start, end = strs[0], strs[len(strs)-1]
        # for i in range(len(start)):
        #     if start[i] != end[i]:
        #         return start[:i]
        # else:
        #     return start

        # length, count = len(strs[0]), len(strs)
        # for i in range(length):
        #     c = strs[0][i]
        #     if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
        #         return strs[0][:i]
        # return strs[0]

        def lcp(start, end):
            if start == end:
                return strs[start]
            mid = (start + end) // 2
            lcpLeft, lcpRight = lcp(start, mid), lcp(mid+1, end)
            minLength = min(len(lcpLeft), len(lcpRight))
            for i in range(minLength):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]
            return lcpLeft[:minLength]
        return '' if not strs else lcp(0, len(strs)-1)


if __name__ == "__main__":
    test = ["aba", "ab", "aba"]
    print(Solution.longestCommonPrefix(test))
