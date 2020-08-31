"""
day: 2020-08-30
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xdapzt/
题目名: 通配符匹配
给定一个字符串(s)和一个字符模式(p),实现一个支持'?'和'*'的通配符匹配
    '?'可以匹配任何单个字符
    '*'可以匹配任意字符串(包括空字符串)
两个字符串完全匹配才算匹配成功
示例:
    输入: s='aa', p='a'
    输出: false
    输入: s='aa', p='*'
    输出: true
思路:
1. 动态规划
    对于s的前i个字符与p的前j个字符,它们之间只会有两种情况:
        1. 匹配 -> true
        2. 不匹配->false
    对于p的第j个字符,dp[i][j]的状态应该为:
        当p是小写字符时,当s[i] == p[j]时, dp[i][j] = dp[i-1][j-1]
        否则为false.
        当p是?时,dp[i][j] = dp[i-1][j-1]
        当p是*时,对于星号,我们有两种情况,一种是在之前使用了这个星号,那么
        dp[i][j] = dp[i-1][j],如果之前没使用这个星号,那么dp[i][j] = dp[i][j-1]
        只要其中有一个是true,那么dp[i][j]就是可以匹配的,所以dp[i][j] = dp[i-1][j] | dp[i][j-1]
    对一些特殊情况的讨论:
        对于dp[0][0],也就是s和p都为空字符串时,他们是必定匹配的.
        对于dp[i][0],也就是p为空,s不为空时,他们是必定不匹配的
        对于dp[0][j],也就是s为空,p不为空时,只有p全由星号组成,他们才匹配.
2. 贪心算法
    对于p : *abc*e*df*
    我们只需要在s中找是否有abc的子串,然后从下一位开始找是否有e的子串,然后从下一位找是否有df的子串,,
    这样说明p和s可以匹配
    我们定义两个指针s_index和p_index来遍历两个字符串,并定义两个指针s_record和p_record来记录子串匹配的开始的位置,当我们遇到*时,
    那么就将p_index后移一位,然后让s_record与p_record记录当前index的位置,最后开始匹配,这表示用*匹配一个空字符串
    如果在匹配的过程中,出现了两边字符不相等的情况,那么我们就使用*往后匹配一位,接着从下一个位置开始重新匹配

    为了处理开头的*与结尾的*,我们可以在开始时就匹配字符串结尾的字符,让结尾的字符指向最后一个*,而对于开头的*,我们将record的初值设置为-1,
    若在record为-1时,出现了字符不匹配的情况,那么说明整个字符串都不匹配,直接返回false
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s = len(s)
        len_p = len(p)
        dp = [[False] * (len_s+1) for _ in range(len_p+1)]
        # 两个字符串长度都为0时,匹配必定成功
        dp[0][0] = True
        # 对于长度为j的字符串,要想匹配长度为0的字符串s,必须全都由*组成
        for j in range(1, len_p+1):
            if p[j-1] == '*':
                dp[0][j] = True
            else:
                break
        for i in range(1, len_s+1):
            for j in range(1, len_p+1):
                # 如果末尾的字符是*,所有字符都可以匹配
                if p[j-1] == '*':
                    # i-1表示使用*字符,j-1表示不使用*字符
                    dp[i][j] = dp[i-1][j] | dp[i][j-1]
                # p[j]为?,说明本次匹配必定成功,那么本次的状态就是前面一格的状态
                elif p[j-1] == '?' or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
        return dp[len_s][len_p]

    def isMatch_greedy(self, s: str, p: str) -> bool:
        def charMatch(s_chr, p_chr):
            return s_chr == p_chr or p_chr == '?'
        s_right = len(s)
        p_right = len(p)
        # 从结尾开始将所有非*的字符串匹配完成
        while s_right > 0 and p_right > 0 and p[p_right-1] != '*':
            if charMatch(s[s_right-1], p[p_right-1]):
                s_right -= 1
                p_right -= 1
            else:
                return False
        # 如果正则字符串已经匹配完了
        # 判断原字符串是否还有未匹配的字符,有则说明无法完全匹配
        if p_right == 0:
            return s_right == 0

        s_index = p_index = 0
        # s_record记录的是s与p进行子串匹配的起始位置
        # p_record记录的是上一个星号所在的位置
        s_record = p_record = -1
        # 开始从头匹配剩余的s与p
        while s_index < s_right and p_index < p_right:
            # 如果p当前的字符是*,那么从下一个字符开始
            # 匹配s与p的子串字符
            if p[p_index] == '*':
                p_index += 1
                s_record, p_record = s_index, p_index
            # 如果匹配则继续匹配下一个字符
            elif charMatch(s[s_index], p[p_index]):
                s_index += 1
                p_index += 1
            # 否则,判断在这之前是否遇到了*
            # 如果遇到的话,就让*匹配的s字符多一位,然后继续
            # 从后一位匹配s与p的子串字符
            elif s_record != -1 and s_record < s_right:
                # 把s子串的起始位置后移一位
                s_record += 1
                # 后退到重新匹配子串
                s_index, p_index = s_record, p_record
            else:
                return False
        # 剩余的未匹配完的字符,只有*可以匹配,所以判断剩余的字符是否
        # 全为*
        return all(p[i] == '*' for i in range(p_index, p_right))


if __name__ == "__main__":
    test_p = '*a*b?'
    test_s = 'beabc'
    s = Solution()
    print(s.isMatch_greedy(test_s, test_p))
