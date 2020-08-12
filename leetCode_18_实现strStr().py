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
1. 遍历字符串,每次从haystack字符串使用切片截取与needle等长的字符串,对比是否相等
优化思路:首字母不相等则直接跳过,记录匹配的字符串长度curr_len,每次循环结束回退curr_len-1个字符
2. Sunday算法
    算法的核心思想是,在发现不匹配时,尽可能跳过多的字符来进行下一步的匹配
    在开始,我们需要对needle进行预处理,记录字符串中每一种字符最后出现的位置,保存在字典中
    假设我们这次匹配haystack[i:i+len(needle)+1] != needle,那么haystack[i+len(neddle)+1]
    必定会参加下一轮的匹配,我们将haystack[i+len(neddle)+1]到字典中寻找它最后一次出现的位置
    然后根据位置来将我们的i进行偏移,比如最后一次出现的位置在字符串中的倒数第二位,那么就需要将i
    向右偏移2位..如果这个字符不在字典中,则向右偏移len(neddle)+1位
"""


class Solution:
    @staticmethod
    def strStr(haystack: str, needle: str) -> int:
        length_1 = len(haystack)
        length_2 = len(needle)

        # 解法1
        # 当length_1小于length_2时,直接结束循环跳到else
        # for index in range(length_1-length_2+1):
        #     if haystack[index:index+length_2] == needle:
        #         return index
        # else:
        #     return -1

        # 解法1优化版
        # if length_2 == 0:
        #     return 0
        # x = 0
        # while x < (length_1-length_2+1):
        #     while x < (length_1-length_2+1) and haystack[x] != needle[0]:
        #         x += 1

        #     curr_len = y = 0
        #     while y < length_2 and x < length_1 and haystack[x] == needle[y]:
        #         x += 1
        #         y += 1
        #         curr_len += 1

        #     if curr_len == length_2:
        #         return x - length_2

        #     x = x - curr_len + 1
        # else:
        #     return -1

        # 解法2 Sunday解法
        def calShiftMat(st):
            dic = {}
            for i in range(len(st)-1, -1, -1):
                if not dic.get(st[i]):
                    dic[st[i]] = len(st) - i
            dic['ot'] = len(st) + 1
            return dic

        # 其他情况判断
        if length_1 < length_2:
            return -1
        elif length_2 == 0:
            return 0

        dic = calShiftMat(needle)
        idx = 0

        while idx <= length_1-length_2:
            str_cut = haystack[idx: idx+length_2]
            if str_cut == needle:
                return idx
            else:
                if idx >= length_1 - length_2:
                    return -1
                cur_c = haystack[idx+length_2]
                if dic.get(cur_c):
                    idx += dic[cur_c]
                else:
                    idx += dic['ot']

        return -1 if idx >= length_1-length_2 else idx


if __name__ == "__main__":
    test1 = "mississippi"
    test2 = "sippj"
    print(Solution.strStr(test1, test2))
