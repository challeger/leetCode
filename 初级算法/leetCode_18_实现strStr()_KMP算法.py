"""
day: 2020-08-12
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnr003/
题目名: 实现strStr()
题目描述: 给定一个haystack字符串和一个needle字符串,在haystack字符串中找出needle字符串出现的第一个位置,如果不存在则返回-1
示例:
    输入: haystack = "hello", needle = "ll"
    输出: 2

    输入: haystack = "aaaaa", needle = "bba"
    输出: -1
思路:
KMP算法:
    设文本串为txt, 匹配串为pat
    文本串的长度为M, 匹配串的长度为L
算法流程:
    根据pat,获得next数组,next数组中的值代表当前字符之前的字符串中
    相同前后缀的最大长度
    在pat与txt匹配时,若在某个字符匹配失败,那么根据当前pat的index-1去
    next数组中找到对应的值,这个值对应的是在pat[index]这个字符前的字符串中,相同前后缀
    的最大长度是多少,根据这个长度x,我们在下一次匹配时,就可以从pat[x]开始,与当前txt指针指向
    的字符去匹配,pat[x]字符前面的字符串因为前后缀相同,所以是必定相等的.
    例如:
    txt = "abcxabcdabxabcdabcdabcy"
    pat = "abcdabcy"
    next = [0, 0, 0, 0, 1, 2, 3, 0]
    当我们匹配到txt[3]与pat[3]时,两个字符并不相等,
    那么就会根据next[2]中的值,将txt[3]与pat[0]进行匹配,
    pat指针指向首部且与txt指针指向的字符匹配不上时
    会将txt的指针向右移一位,就会将txt[4]与pat[0]进行匹配
    接下来会一直匹配到txt[10]和pat[6],
    根据next[5]中的值2,很显然pat[:2]==txt[8:10],我们可以直接从pat[2]开始与txt[10]匹配
    但pat[2]与txt[10]的值并不相等,所以根据next[1]中的值,将txt[10]与pat[0]匹配,依旧不相等,
    此时pat指针已经指向首部了,所以将txt指针右移一位,一直匹配到
    txt[18]和pat[7],根据next[6]中的值3,直接用pat[3]与txt[18]匹配,相等,最终匹配到完整字符串
算法核心:
    根据pat计算出next数组:
    pat  = a, a, a, d, a, a, a, a
    next = 0, 1, 2, 0, 1, 2, 3, 3

next数组计算流程:
    i->遍历数组的指针
    j->在i之前的字符串中,相同前后缀的最大长度
    每次遍历都会在next[i]中放入j的值
    因为单个字符是没有真前后缀的,所以i从1开始,而j则从0开始
    i = 1, j = 0:
        pat[i](a) == pat[j](a)  --> i右移一位, j+1=1, next = [0, 1]
    i = 2, j = 1:
        pat[i](a) == pat[j](a)  --> i右移一位, j+1=2, next = [0, 1, 2]
    i = 3, j = 2:
        pat[i](d) != pat[j](a)  --> 根据next[j-1]获取匹配失败前的相同前后缀的最大长度,让j指向相同前后缀字符串的下一个字符
    i = 3, j = 1:
        pat[i](d) != pat[j](a)  --> 根据next[j-1]获取匹配失败前的相同前后缀的最大长度,让j指向相同前后缀字符串的下一个字符
    i = 3, j = 0:
        pat[i](d) != pat[j](a)  --> i右移一位, j不变=0, next = [0, 1, 2, 0]
    i = 4, j = 0:
        pat[i](a) == pat[j](a)  --> i右移一位, j+1=1, next = [0, 1, 2, 0, 1]
    i = 5, j = 1:
        pat[i](a) == pat[j](a)  --> i右移一位, j+1=2, next = [0, 1, 2, 0, 1, 2]
    i = 6, j = 2:
        pat[i](a) == pat[j](a)  --> i右移一位, j+1=3, next = [0, 1, 2, 0, 1, 2, 3]
    i = 7, j = 3:
        pat[i](a) != pat[j](d)  --> 根据next[j-1]获取匹配失败前的相同前后缀的最大长度,让j指向相同前后缀字符串的下一个字符
    i = 7, j = 2:
        pat[i](a) == pat[j](a)  --> j+1=3, next = [0, 1, 2, 0, 1, 2, 3, 3], 完成遍历

字符串匹配流程:
    txt = "abcxabcdabxabcdabcdabcy"
    pat = "abcdabcy"
    next = [0, 0, 0, 0, 1, 2, 3, 0]

    i->txt的指针
    j->pat的指针
    当txt[i]与pat[j]不相等时,会根据next[j-1]也就是j指向的字符前面的字符串的相同前后缀的最大值,
    来决定从pat的哪一个字符开始与txt[i]进行匹配,直到j指向pat的首部,若j指向pat的首部时,txt[i]与
    pat[j]还是不相等,则将i向右移一位,继续与pat[j]匹配
    i, j = 0, 0:
        txt[i] = a, pat[j] = a -> 相等,i与j都后移一位
    一直匹配到
    i, j = 3, 3:
        txt[i] = x, pat[j] = d -> 不相等,j!=0, 所以j=next[j-1]=0,i不变
    i, j = 3, 0:
        txt[i] = x, pat[j] = a -> 不相等,j==0, 所以i右移一位
    i, j = 4, 0:
        txt[i] = a, pat[j] = a -> 相等, i与j都后移一位
    一直匹配到
    i, j = 10, 6:
        txt[i] = x, pat[j] = c -> 不相等,j!=0, 所以j=next[j-1]=2,i不变
    i, j = 10, 2:
        txt[i] = x, pat[j] = c -> 不相等,j!=0, 所以j=next[j-1]=0,i不变
    i, j = 10, 0:
        txt[i] = x, pat[j] = a -> 不相等,j==0, 所以i右移一位
    i, j = 11, 0:
        txt[i] = a, pat[j] = a -> 相等, i与j都后移一位
    一直匹配到
    i, j = 18, 7:
        txt[i] = d, pat[j] = y -> 不相等, j!=0, 所以j=next[j-1]=3,i不变
    i, j = 18, 3:
        txt[i] = d, pat[j] = d -> 相等, i与j都后移一位
    一直到匹配完成,最终返回 i - j = 15
"""


class Kmp:
    def __init__(self, pat):
        super().__init__()
        self.pat = pat
        self.M = len(pat)
        self.dp = []
        self.set_dp()

    def set_dp(self):
        # 第一个字符没有真前后缀,直接置0
        self.dp.append(0)
        i, j = 1, 0
        while i < self.M:
            if self.pat[i] == self.pat[j]:
                # 相等则相同前后缀长度+1
                j += 1
                # 放入next数组中
                self.dp.append(j)
                # 指针右移一位
                i += 1
            else:
                # 不相等时
                if j == 0:
                    # 前面的字符串的相同前后缀长度为0
                    self.dp.append(0)
                    # 指针右移一位
                    i += 1
                else:
                    # 前面的字符串的相同前后缀长度不为0
                    # 则从相同前后缀的下一个字符进行匹配
                    j = self.dp[j-1]

    def search(self, txt):
        N = len(txt)
        # 匹配的状态
        i = j = 0
        while i < N:
            # 如果两个字符相等,则两个指针都向右移一位
            if txt[i] == self.pat[j]:
                i += 1
                j += 1
            else:
                if j != 0:
                    # 如果pat的指针不指向首部,则去指向最大相同前后缀字符串的下一个字符
                    j = self.dp[j-1]
                else:
                    # 如果pat的指针指向首部,则txt的指针右移一位
                    i += 1
            # 若一直匹配到了尾部,则说明匹配完成
            if j == self.M:
                return i - j
        return -1


class Solution:
    @staticmethod
    def strStr(haystack: str, needle: str) -> int:
        # 进行一些预处理
        if len(haystack) < len(needle):
            return -1
        elif not needle:
            return 0
        kmp = Kmp(needle)
        return kmp.search(haystack)


if __name__ == "__main__":
    test1 = "abcxabcdabxabcdabcdabcy"
    test2 = "abcdabcy"
    print(Solution.strStr(test1, test2))
