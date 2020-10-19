"""
day: 2020-10-19
url: https://leetcode-cn.com/problems/backspace-string-compare/
题目名: 比较含退格的字符串
给定S和T两个字符串,当它们分别被输入到空白的文本编辑器后,判断两者是否相等
并返回结果.
'#'代表退格字符

思路:
1. 栈
    遇到非'#'字符就推入栈中,遇到'#'就推出栈顶,最后判断是否相等
2. 双指针
    定义两个指针分别从两个字符串的尾部开始遍历,每次都保证当前指针指向
    的字符不是'#', 如果是'#'则需要将指针继续前移
"""


class Solution:
    def backspaceCompare_1(self, S: str, T: str) -> bool:
        lst_s = []
        lst_t = []
        for char in S:
            if char != '#':
                lst_s.append(char)
            elif lst_s:
                lst_s.pop()
        for char in T:
            if char != '#':
                lst_t.append(char)
            elif lst_t:
                lst_t.pop()
        return lst_s == lst_t

    def backspaceCompare(self, S: str, T: str) -> bool:
        idx_s = len(S) - 1  # 字符串S的指针
        idx_t = len(T) - 1  # 字符串T的指针
        back_s = back_t = 0  # 表示需要退格的数量
        while idx_s >= 0 or idx_t >= 0:
            while idx_s >= 0:
                if S[idx_s] == '#':
                    back_s += 1
                elif back_s > 0:
                    back_s -= 1
                else:
                    break
                idx_s -= 1
            while idx_t >= 0:
                if T[idx_t] == '#':
                    back_t += 1
                elif back_t > 0:
                    back_t -= 1
                else:
                    break
                idx_t -= 1
            if idx_s >= 0 and idx_t >= 0:
                if S[idx_s] != T[idx_t]:
                    return False
            elif idx_s >= 0 or idx_t >= 0:
                return False
            idx_s -= 1
            idx_t -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.backspaceCompare("bbbextm", "bbb#extm"))
