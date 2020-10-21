"""
day: 2020-10-21
url: https://leetcode-cn.com/problems/long-pressed-name/
题目名: 长按键入
你的朋友正在使用键盘输入他的名字name,偶尔在键入字符c时,按键可能会被长按,而
字符可能被输入1次或者多次
你将会检查键盘输入的字符typed.如果它对应的可能是你的朋友的名字,那么就返回True
思路:
    双指针分别指向两个字符串,如果字符相等就往后移,不相等则判断指向typed的指针,
    当前的值是否与上一个值相等,相等说明是长按键入,否则就返回False

    在某个指针遍历完成之后,退出循环,首先判断typed是否遍历完成,若未完成还得判断
    剩余的字符是否全部相等,否则是错误的

    最后判断指向name的指针是否指向尾部即可.
"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        len_1 = len(name)
        len_2 = len(typed)
        if len_1 > len_2:
            return False
        idx_1 = 0
        idx_2 = 0
        while idx_1 < len_1 and idx_2 < len_2:
            if name[idx_1] == typed[idx_2]:
                idx_1 += 1
                idx_2 += 1
            elif idx_2 > 0 and typed[idx_2] == typed[idx_2-1]:
                idx_2 += 1
            else:
                return False
        while idx_2 < len_2:  # 判断可能存在的剩余部分
            if typed[idx_2] != typed[idx_2-1]:
                return False
            idx_2 += 1
        return idx_1 == len_1
