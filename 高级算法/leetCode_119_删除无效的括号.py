"""
day: 2020-08-30
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xdm2sj/
题目名: 删除无效的括号
删除最小数量的无效括号,使得输入的字符串有效,返回所有可能的结果
说明: 输入可能包含了除()以外的字符
示例:
    输入: "()())()"
    输出: ["()()()", "(())()"]
    输入: "(a)())()"
    输出: ["(a)()()", "(a())()"]
    输入: ")("
    输出: [""]
思路:
1. BFS
    对于节点s,它删除某一个括号构成的字符串,就是它的下一层需要遍历的节点,所以我们可以使用BFS,
    从字符串s开始,每次遍历将该层的所有节点删除一个括号的产生的结果加入下一层中,直到我们遇到了一个
    合法的括号字符串,那么说明该层就是删除最小数量的括号层,于是我们将正确的结果全部加入res中,然后返回即可
2. DFS
    对于一个无效的括号字符串,我们想以最小数量删除括号来得到一个合法的字符串,那么只需要将左边的括号数量变成与
    右边括号数相等即可,那么我们先求出需要删除的最小数量,然后根据这个数量进行深度遍历,直到左括号数与右括号数
    相等,然后判断该字符串是否是一个合法的括号字符串,是则加入结果中
"""
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(str):
            cnt = 0
            # 对于一个合法的括号字符串
            # 它的左右括号数应该是相等的,并且右边括号永远小于等于左边括号
            for foo in str:
                if foo == '(':
                    cnt += 1
                elif foo == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        level = {s}
        while level:
            # 判断在当前层中,是否有符合要求的字符串,有的话,那么
            # 该层就是我们要找的删除无效括号最小的结果
            valid = list(filter(is_valid, level))
            if valid:
                return valid
            next_level = set()
            # 下一层的节点是当前层的节点的所有剪切结果
            for item in level:
                for i in range(len(item)):
                    # 如果是括号,就把 将该位删去的字符串添加到下一层节点中
                    if item[i] in '()':
                        next_level.add(item[:i] + item[i+1:])
            level = next_level
        return ['']

    def removeInvalidParentheses_dfs(self, s: str) -> List[str]:
        def is_valid(str):
            cnt = 0
            # 对于一个合法的括号字符串
            # 它的左右括号数应该是相等的,并且右边括号永远小于等于左边括号
            for foo in str:
                if foo == '(':
                    cnt += 1
                elif foo == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        def dfs(string, idx, re_left, re_right):
            # 如果括号数删完了,判断当前的字符串是否是一个合法的括号字符串.
            # 是则加入结果中
            if not re_left and not re_right:
                if is_valid(string):
                    ans.add(string)
                return

            for i in range(idx, len(string)):
                if re_left > 0 and string[i] == '(':
                    dfs(string[:i] + string[i+1:], i, re_left-1, re_right)
                elif re_right > 0 and string[i] == ')':
                    dfs(string[:i] + string[i+1:], i, re_left, re_right-1)

        left = right = 0
        ans = {}
        # 这里求出将字符串变为合法的括号字符串
        # 需要删除的最小的左括号数与右括号数
        for chr in s:
            if chr == '(':
                left += 1
            elif chr == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        dfs(s, 0, left, right)
        return ans


if __name__ == "__main__":
    test = "(()()))"
    s = Solution()
    print(s.removeInvalidParentheses(test))
