"""
day: 2020-08-25
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xw1tws/
题目名: 滑动窗口最大值
给你一个字符串S,一个字符串T.请你设计一种算法,可以在O(n)的时间复杂度内,从字符串S里面找出包含
T所有字符的最小子串
    如果S中不存在这样的子串,则返回空字符串''
示例:
    输入: S='ADOBECODEBANC', T='ABC'
    输出: 'BANC'
思路:
滑动窗口
    用left来表示左边界,right表示右边界..
    1.让right不断增加,使窗口增大,直到窗口中包含了T中的所有元素
    2.让left不断增加,使窗口缩小,直到碰到一个必须包含的元素,记录长度,获取最小值
    3.让left再增加一位,这时窗口必然不满足步骤1,所以我们接着执行步骤1,直到找到下一个窗口..
    如此反复,直到right超出了s的范围.

    需要解决的问题:
        如何判断是否包含了T中的所有元素?
            用一个哈希表need_count,键为T中的字符串,值为出现的次数,然后再定义一个变量need_char=len(T)
            在我们遍历S时,判断need_count[c]大于0,大于0说明需要这个字符串,于是need_char -= 1
            无论是否大于0, 对于need_count[c]我们都需要进行减1操作,来排除无用元素
        如何排除无用元素?
            在我们找到满足条件的窗口后,我们开始收缩左窗口,每次我们判断need_count[s[left]]==0,
            是的话说明s[left]是一个必须元素,如果小于0,那么它是一个无用元素,为了排除重复元素的影响
            我们将need_count[s[left]]+1后,再收缩左窗口..直到找到必须元素
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        need_count = defaultdict(int)
        for c in t:
            need_count[c] += 1
        need_char = len(t)
        left = 0
        res = [0, float('inf')]
        for right, c in enumerate(s):
            # 不断移动右窗口,直到t中的所有元素都被找到
            if need_count[c] > 0:
                need_char -= 1
            need_count[c] -= 1
            # 长度为0说明需要的字符全都找到了
            if not need_char:
                # 移动左窗口,将非必须的元素排除
                while True:
                    foo = s[left]
                    # 为0说明当前的字符是必须的
                    if need_count[foo] == 0:
                        break
                    # 因为可能会有重复的元素出现,所以当我们滑动左窗口时
                    # 需要将对应的元素需要的数量+1
                    need_count[foo] += 1
                    # 滑动左窗口
                    left += 1
                # 判断最小值
                if right-left < res[1]-res[0]:
                    res = [left, right]
                # 再将左窗口右移一位,然后接着去找下一个满足条件的字符串
                need_count[s[left]] += 1
                need_char += 1
                left += 1
        return '' if res[1] > len(s) else s[res[0]:res[1]+1]


if __name__ == "__main__":
    test1 = 'ADOBECODEBANC'
    test2 = 'ABC'
    s = Solution()
    print(s.minWindow(test1, test2))
