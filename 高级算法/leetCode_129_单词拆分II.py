"""
day: 2020-09-02
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xdl705/
题目名: 单词拆分II
给定一个非空字符串s和一个包含非空单词列表的字典wordDict,在字符串中增加空格来构建一个句子,使得
句子中所有的单词都在词典中,返回所有这些可能的句子
    1. 拆分时可以重复使用字典中的单词
    2. 你可以假设字典中没有重复的单词
示例:
    输入: s = 'leetcode', wordDict = ['leet', 'code']
    输出: ['leet code']
    输入: s = 'catsandog', wordDict = ['cats', 'dog', 'sand', 'and', 'cat']
    输出: ['cats and dog', 'cat sand dog']
思路:
1. 先预处理判断字符串能否被拆分,可以的话就倒序dfs插入list中,当全部插入完时,就将当前的
list拼接成字符串添加到结果中
2. 预处理判断字符串能否被拆分,若能,定义一个dp数组,dp[i]表示字符串s的前i个字符,全部由wordDict
中的单词组成的句子,
对于当前的dp[i],我们定义一个指针j,遍历[0:i],如果dp[j]有数据,那么判断s[i:j]是否在wordDict中,在
的话就将dp[j]与s[i:j]组成新的句子,添加到dp[i]中..
需要注意的是,对于dp[0],它的内容应该是[''],这样做是为了在添加第一个单词时,不会因为dp[0]中没有内容而不进行添加
"""
from typing import List
from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordDict = set(wordDict)
        # 先进行预处理,判断该字符串能否被分割
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(n+1):
            for j in range(i):
                # 如果0:j是true,且s[j:i]在wordDict中,那么dp[i]就是true
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        res = []
        # 可以被分割
        if dp[-1]:
            def dfs(end, path):
                # 如果剩余的单词都在,那么就添加结果
                if s[:end+1] in wordDict:
                    path.appendleft(s[:end+1])
                    res.append(' '.join(path))
                    path.popleft()
                # 倒序遍历
                for i in range(end, 0, -1):
                    # 如果前i个字符可以被分割
                    if dp[i]:
                        fuck = s[i:end+1]
                        # 判断i到end的单词是否在单词本中
                        if fuck in wordDict:
                            # 在则分割,并将指针移动到i前一个字符
                            # 进行下一层遍历
                            path.appendleft(fuck)
                            dfs(i-1, path)
                            path.popleft()

            queue = deque()
            dfs(n-1, queue)
        return res

    def wordBreak_dp(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        # dp[i]表示前i个字符中,由wordDict组成的全部可能的句子
        dp = [[] for _ in range(n+1)]
        wordDict = set(wordDict)
        dp[0] = {''}
        for i in range(1, n+1):
            temp = []
            for j in range(i):
                # 如果前j个字符可以组成句子,并且 s[j:i]也在单词本中
                if dp[j] and s[j:i] in wordDict:
                    # 那么将s[j:i]与dp[j]中的所有句子组成新的句子,添加到当前的dp[i]中
                    for foo in dp[j]:
                        # 如果前面是一个空字符串,那么不应该添加空格
                        temp.append(foo + ('' if not foo else ' ') + s[j:i])
            dp[i] = temp
        return dp[-1]


if __name__ == "__main__":
    test = 'catsanddog'
    words = ["cats", "dog", "sand", "and", "cat"]
    s = Solution()
    print(s.wordBreak_dp(test, words))
