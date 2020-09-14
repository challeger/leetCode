"""
day: 2020-09-14
url: https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
题目名: 串联字符串的最大长度
给定一个字符串数组 arr,字符串 s 是将 arr 某一子序列字符串连接所得的字符串
如果 s 中的每一个字符都只出现过一次,那么它就是一个可行解。
请返回所有可行解 s 中最长长度

示例:
    输入：arr = ["un","iq","ue"]
    输出：4
思路:
    深度遍历,判断每一种可能性.
"""
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def is_repeat(s):
            return len(s) == len(set(s))
        res = 0
        n = len(arr)

        def dfs(index, path):
            nonlocal res
            if index >= n:
                res = max(res, len(path))
                return
            foo = path + arr[index]
            if is_repeat(foo):
                dfs(index+1, foo)
            dfs(index+1, path)
        dfs(0, '')
        return res
