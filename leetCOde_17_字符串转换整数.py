"""
day: 2020-08-12
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnoilh/
题目名: 字符串转换整数
题目描述: 实现一个函数,使其能将字符串转换为整数
转换规则:
    1. 如果第一个非空字符串为正或者负号时, 则将该符号与之后尽可能多的连续数字字符组合起来,组成一个有符号整数
    2. 如果第一个非空字符是数字,则直接将其与之后连续的数字字符组合起来,形成一个整数
    3. 如果整数部分之后有多余的字符,那么这些字符可以被忽略
    4. 如果第一个非空字符串既不是正负号,也不是数字,则返回0
    5. 如果不能进行有效的转换,返回0
    6. 如果数值超过[-2^31, 2^31-1],返回INT_MAX或INT_MIN
示例:
    输入: "42"
    输出: 42

    输入: "   -42"
    输出: -42

    输入: "4396 is clearlove"
    输出: 4396

    输入: "xiaohu 2200"
    输出: 0

    输入: "-91283472332"
    输出: -2147483648
思路:
1. 使用正则表达式提取出我们想要的数据,然后转换类型,利用max与min来进行溢出处理,int(*[]) = 0
2. 遍历字符串,当遇到非数字字符且不是(+, -)符号,亦或者是(+, -)符号但不在字符串首部的,退出循环
然后转换类型
"""


class Solution:
    @staticmethod
    def myAtoi(s: str) -> int:
        INT_MAX = (1 << 31) - 1
        INT_MIN = (-1 << 31)

        import re
        return min(max(int(*re.findall(r'^[+-]?\d+', s.lstrip())), INT_MIN), INT_MAX)

        # s = s.lstrip()  # 去除空格
        # result = 0
        # foo = ''
        # index = 0
        # while (index < len(s)) and (s[index].isdigit() or (s[index] in ('+', '-') and index == 0)):
        #     foo += s[index]
        #     index += 1

        # if len(foo) == 1 and not foo.isdigit():
        #     return 0

        # result = int(foo) if foo else 0
        # return min(max(result, INT_MIN), INT_MAX)


if __name__ == "__main__":
    test = '+-2'
    print(Solution.myAtoi(test))
