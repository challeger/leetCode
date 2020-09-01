"""
day: 2020-09-01
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xd7u77/
题目名: 单词拆分
给定一个非空字符串s和一个包含非空单词列表的字典wordDict,判定s是否可以被空格拆分为一个或多个在
字典中出现的单词
    1. 拆分时可以重复使用字典中的单词
    2. 你可以假设字典中没有重复的单词
示例:
    输入: s = 'leetcode', wordDict = ['leet', 'code']
    输出: true
    输入: s = 'catsandog', wordDict = ['cats', 'dog', 'sand', 'and', 'cat']
思路:
"""
from typing import List
from collections import deque


class Solution:
    def wordBreak_bfs(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        # 记忆化访问
        visited = [False for _ in range(len(s))]
        queue = deque()
        queue.append(0)
        while queue:
            size = len(queue)
            for _ in range(size):
                fuck = queue.popleft()
                # 如果该节点在之前某次遍历时已经访问过
                # 那么说明该节点可能得到的值已经在队列中了
                # 所以无需再次计算,直接跳过.
                if visited[fuck]:
                    continue
                # 否则将当前节点设置为已访问
                visited[fuck] = True
                for i in range(fuck+1, len(s)+1):
                    if s[fuck:i] in wordDict:
                        if i == len(s):
                            return True
                        queue.append(i)
        return False

    def wordBreak_dp(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        # dp表示对于dp的前i个字符,能否将其分割为由wordDict中的单词组成的
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(n+1):
            for j in range(i):
                # 如果0:j是true,且s[j:i]在wordDict中,那么dp[i]就是true
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]

    def wordBreak_dfs(self, s: str, wordDict: List[str]) -> bool:
        from functools import lru_cache

        wordDict = set(wordDict)
        n = len(s)

        # 记忆函数的计算结果,在访问同样结果时直接返回结果
        @lru_cache(None)
        def dfs(idx):
            if idx > n - 1:
                return True
            for i in range(idx+1, n+1):
                if s[idx:i] in wordDict and dfs(i):
                    return True
            return False
        return dfs(0)


if __name__ == "__main__":
    test = 'catsandog'
    words = ["cats", "og", "sand", "and", "cat"]
    s = Solution()
    print(s.wordBreak_dfs(test, words))
